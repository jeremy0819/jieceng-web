# 傑丞建築機構 官網

為「傑丞建築機構」打造的高級感建築形象網站，採用 **Nuxt 3** 靜態網站生成（SSG），透過極簡留白與優雅動態，傳遞品牌的專業工法與空間美學。

## 技術棧

- **Nuxt 3 / Vue 3** — SSG 靜態產生，部署後純靜態檔案、載入快、利於 SEO
- **Tailwind CSS**（`@nuxtjs/tailwindcss`）— 設計系統與樣式
- **GitHub Pages + GitHub Actions** — 推送即自動部署

## 視覺基因（Visual DNA）

設計調整時請遵守以下規範（定義於 `tailwind.config.js` 與 `assets/css/main.css`）：

| 項目 | 值 | 用途 |
| --- | --- | --- |
| 暖米白 `#fafaf9` | `warm-white` | 全局背景 |
| 深炭黑 `#1a1a1a` | `charcoal` | 主文字與線條 |
| 翡翠綠 `#064e3b` | `emerald-brand` | 品牌色、點綴、選取效果 |

- **字體**：`Playfair Display`（襯線體大標題）、`Inter`（無襯線內文）、`JetBrains Mono`（技術數據／編號）
- **動態曲線**：`cubic-bezier(0.16, 1, 0.3, 1)`，時長 1.2s（`transition-*` 的 `elegant` / `duration-1200`）

## 專案結構

```text
.
├── .github/workflows/deploy.yml  # GitHub Pages 自動部署流程
├── assets/css/main.css           # 全局樣式、捲軸與選取色客製化
├── components/
│   ├── TheNavbar.vue             # 導覽列（滾動毛玻璃效果）
│   └── TheFooter.vue             # 頁尾
├── composables/
│   └── useProjects.ts            # ★ 作品資料的單一來源
├── layouts/default.vue           # 基礎佈局（頁面過渡、自動回頂）
├── pages/
│   ├── index.vue                 # 首頁（Hero + 精選作品）
│   ├── about.vue                 # 關於我們
│   ├── pcm.vue                   # 全案管理 PCM
│   ├── portfolio.vue             # 作品集（分類過濾）
│   ├── contact.vue               # 聯絡方式
│   └── project/[id].vue          # 作品詳情（動態路由）
├── public/image/                 # 圖片資源
├── nuxt.config.ts                # Nuxt 設定（SSG、字體、baseURL）
└── tailwind.config.js            # 品牌色與自定義動畫
```

## 本機開發

需求：Node.js 20 以上。

```bash
npm install        # 安裝依賴
npm run dev        # 啟動開發伺服器 http://localhost:3000
```

## 建置與預覽（產出靜態檔案）

```bash
npm run generate            # 產生靜態網站到 .output/public
npx serve .output/public    # 本機預覽產出結果
```

## 新增一個作品

作品資料集中在 [`composables/useProjects.ts`](composables/useProjects.ts)，首頁、作品集、詳情頁都會自動同步。新增步驟：

1. 把圖片放到 `public/image/`，例如 `project-5.jpg`（請用英文小寫檔名）。
2. 在 `useProjects.ts` 的陣列加一筆物件（`id`、`title`、`category`、`description`、`fullDescription`、`image`、`specs`）。
3. 在 `nuxt.config.ts` 的 `nitro.prerender.routes` 加上 `'/project/5'`，確保該頁會被預先產生。

## 部署到 GitHub Pages

1. 建立 GitHub 倉庫並推送本專案（見下方步驟）。
2. 到倉庫 **Settings → Pages → Build and deployment → Source**，選擇 **GitHub Actions**。
3. 之後每次推送到 `main` 分支，[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) 會自動 build 並發布。

### 關於子路徑（baseURL）

- 專案倉庫（如 `user/jieceng-web`）會部署在 `https://user.github.io/jieceng-web/`，網站需要 `/jieceng-web/` 的路徑前綴。部署流程會**自動**依倉庫名稱設定 `DEPLOY_BASE`，無需手動調整。
- 若使用 `user.github.io` 這種使用者站台（部署在根目錄），流程會自動改用 `/`。
- **注意**：本專案刻意使用自訂的 `DEPLOY_BASE` 而非 `NUXT_APP_BASE_URL`，因為後者會在 prerender 時被重複套用，導致整站變成空白轉址檔。
