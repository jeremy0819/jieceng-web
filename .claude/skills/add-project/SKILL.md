---
name: add-project
description: 新增一個建築作品到網站作品集。當使用者說「新增作品」「加一個案例」「add a project」或想把新的建築專案放上網站時使用。會自動更新作品資料、預先產生路由，並檢查圖片。
---

# 新增作品到作品集

傑丞建築網站的所有作品資料集中在單一檔案，新增一筆就會同步到首頁、作品集頁、建案詳情頁、導覽列下拉選單。請依序完成下列步驟。

## 需要向使用者確認的資訊

開始前，先確認以下欄位都齊全（缺少就詢問使用者；若使用者不在線上，依品牌既有風格與現有建案的寫法補齊並於回覆中說明）：

- **標題** title（慣例格式「傑丞。建案名稱」；都更案可直接用案名，例：新店安和段都更案）
- **分類** category（二選一：`'residential'` 住宅建案、`'renewal'` 都更案）＋對應中文 categoryLabel（`'住宅建案'` / `'都更案'`）
- **年份** year（數字，不加引號）
- **地點** location（例：`'桃園市桃園區'`）
- **短描述** description（一句話，顯示在卡片上，約 20～30 字）
- **完整描述** fullDescription（一段文字，顯示在詳情頁）
- **圖片檔名**（例：`project-5.jpg`，英文小寫）
- **亮點 highlights**（陣列，**固定 4 項**，詳情頁 2×2 版面）
- **規格 specs**（物件，中文 Key 自訂，建議 4 項，例：案件類型／基地位置／導入工法／完工年份）
- **工法標籤 technologies**（陣列，至少 1 項；可用值：`'centennial'` 百年宅、`'healthy'` 健康宅、`'energy'` 節能宅、`'smart'` 智慧宅、`'resume'` 履歷宅）

## 執行步驟

1. **確認圖片** 已放在 `public/image/`。若使用者還沒放，提醒他們把圖片檔放進該資料夾，檔名用英文小寫。

2. **在 `composables/useProjects.ts`** 的 `projects` 陣列最後加一筆物件，`id` 用目前最大 id + 1：

   ```ts
   {
     id: 5,
     title: '傑丞。建案名稱',
     year: 2027,
     category: 'residential',
     categoryLabel: '住宅建案',
     location: '桃園市桃園區',
     description: '卡片用的一句話描述。',
     fullDescription: '詳情頁用的完整段落描述。',
     image: 'image/project-5.jpg',
     highlights: ['亮點一', '亮點二', '亮點三', '亮點四'],
     specs: {
       案件類型: '住宅建案',
       基地位置: '桃園市桃園區',
       導入工法: 'iHome 5.0 全系統',
       完工年份: '2027'
     },
     technologies: ['centennial', 'healthy', 'energy']
   },
   ```

   注意：
   - `image` 路徑開頭**不要**加斜線（用 `image/xxx.jpg`），baseURL 會自動補上。
   - 「卷宗編號」（JC-005 等）會依 id 自動產生，**不需要**手動填寫。

3. **在 `nuxt.config.ts`** 的 `nitro.prerender.routes` 陣列加入對應路由，例如 `'/project/5'`。這一步很重要，漏掉的話該頁部署後會 404。

4. **驗證**：執行 `npm run generate`，確認 build 成功、沒有錯誤，且 `.output/public/project/5.html` 有被產生。

5. **同步維護說明書**：更新 `維護說明書.md` 中的「目前最大 id」「圖片清單」「頁面功能一覽」等對應段落，保持文件與程式一致。

## 完成後

告訴使用者：作品已新增，commit 並 push 到 `main` 分支後，GitHub Actions 會自動部署上線。
