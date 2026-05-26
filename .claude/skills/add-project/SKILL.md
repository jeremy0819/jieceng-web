---
name: add-project
description: 新增一個建築作品到網站作品集。當使用者說「新增作品」「加一個案例」「add a project」或想把新的建築專案放上網站時使用。會自動更新作品資料、預先產生路由，並檢查圖片。
---

# 新增作品到作品集

傑丞建築網站的所有作品資料集中在單一檔案，新增一筆就會同步到首頁、作品集頁、作品詳情頁。請依序完成下列步驟。

## 需要向使用者確認的資訊

開始前，先確認以下欄位都齊全（缺少就詢問使用者）：

- **標題** title（例：開放建築）
- **分類** category（必須是這五個其中之一：`Residential`、`Commercial`、`Landscape`、`Renovation`；若使用者用中文描述，幫忙對應）
- **短描述** description（一句話，顯示在卡片上）
- **完整描述** fullDescription（一段文字，顯示在詳情頁）
- **圖片檔名**（例：`project-5.jpg`，請用英文小寫）
- **規格 specs**：Location、Year、Area、System 四項

## 執行步驟

1. **確認圖片** 已放在 `public/image/`。若使用者還沒放，提醒他們把圖片檔放進該資料夾，檔名用英文小寫。

2. **在 `composables/useProjects.ts`** 的 `projects` 陣列最後加一筆物件，`id` 用目前最大 id + 1：

   ```ts
   {
     id: 5,
     title: '作品標題',
     category: 'Residential',
     description: '卡片用的一句話描述。',
     fullDescription: '詳情頁用的完整段落描述。',
     image: 'image/project-5.jpg',
     specs: {
       Location: '城市, 區域',
       Year: '2026',
       Area: '000 sqm',
       System: '工法名稱',
     },
   },
   ```

   注意 `image` 路徑開頭**不要**加斜線（用 `image/xxx.jpg`），baseURL 會自動補上。

3. **在 `nuxt.config.ts`** 的 `nitro.prerender.routes` 陣列加入對應路由，例如 `'/project/5'`。這一步很重要，漏掉的話該頁部署後會 404。

4. **驗證**：執行 `npm run generate`，確認 build 成功、沒有錯誤，且 `.output/public/project/5.html` 有被產生。

## 完成後

告訴使用者：作品已新增，commit 並 push 到 `main` 分支後，GitHub Actions 會自動部署上線。
