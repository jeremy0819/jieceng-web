
import { GoogleGenAI } from "@google/genai";
import { SYSTEM_PROMPT } from "../constants";

export class GeminiService {
  private getAI() {
    return new GoogleGenAI({ apiKey: process.env.API_KEY || '' });
  }

  async generateChatResponse(userMessage: string, history: { role: 'user' | 'model', parts: { text: string }[] }[] = []) {
    try {
      const ai = this.getAI();
      const userCoords = await new Promise<{lat: number, lng: number} | null>((resolve) => {
        navigator.geolocation.getCurrentPosition(
          (pos) => resolve({ lat: pos.coords.latitude, lng: pos.coords.longitude }),
          () => resolve(null),
          { timeout: 5000 }
        );
      });

      const response = await ai.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [...history, { role: 'user', parts: [{ text: userMessage }] }],
        config: {
          systemInstruction: SYSTEM_PROMPT,
          tools: [{ googleMaps: {} }],
          toolConfig: {
            retrievalConfig: {
              latLng: userCoords ? { latitude: userCoords.lat, longitude: userCoords.lng } : undefined
            }
          }
        }
      });

      return { text: response.text, grounding: response.candidates?.[0]?.groundingMetadata?.groundingChunks || [] };
    } catch (error) {
      console.error("Gemini Error:", error);
      return { text: "目前連線稍有延遲，請稍後再試。", grounding: [] };
    }
  }

  async editImage(prompt: string, base64Image: string, mimeType: string) {
    try {
      const ai = this.getAI();
      const response = await ai.models.generateContent({
        model: 'gemini-2.5-flash-image',
        contents: {
          parts: [{ inlineData: { data: base64Image, mimeType } }, { text: prompt }]
        }
      });
      for (const part of response.candidates?.[0]?.content?.parts || []) {
        if (part.inlineData) return `data:${part.inlineData.mimeType};base64,${part.inlineData.data}`;
      }
      return null;
    } catch (error) {
      console.error("Image Edit Error:", error);
      throw error;
    }
  }
}

export const geminiService = new GeminiService();
