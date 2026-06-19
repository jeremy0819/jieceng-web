# 傑丞建築機構 — 品牌設計速查卡（claude.ai/design 專用）

> 使用方式：在 claude.ai/design 開新設計時，把「給設計代理人的開場白」整段貼進對話框，
> 後面接你要設計的內容（例如：幫我設計一個建案銷售頁）。需要更精準時，再把對應的色彩/字體/視效區塊一起貼上。

---

## ① 給設計代理人的開場白（直接複製這段）

```
請依照「傑丞建築機構」的品牌設計系統來設計。整體風格：高級、沉穩、永續建築精品感，
帶有「建築圖紙」的專業識別語言。請嚴格遵守以下規範：

【色彩】
- 頁面底色用暖象牙白 #f5f3ee（不要用純白）
- 主要文字與深色區塊用深炭色 #1c1a17（不要用純黑）
- 品牌主色深綠 #064e3b（用於按鈕、重點、標題強調）
- 亮綠 #10b981 只用於深色背景上的點綴文字
- 淺綠 #ecfdf5 用於極淺的色塊背景或選取色

【字體】
- 英文/數字標題：Playfair Display（襯線、優雅）
- 中文標題：Noto Serif TC
- 內文：Inter（英）+ Noto Sans TC（中）
- 標籤/編號/技術小字：JetBrains Mono（等寬，常用大寫＋寬字距）
- 中文字距加寬 0.05em，更透氣

【版面氣質】
- 大量留白、克制；標題用細字重（font-light/300）配大字級
- Hero 區用深炭色底，搭配建築實景照（照片可降低透明度、加深色漸層遮罩）
- 卡片用「磨砂玻璃」效果：半透明白底 + 背景模糊 + 細白邊 + 柔和陰影
- 動效優雅緩慢：使用 cubic-bezier(0.16, 1, 0.3, 1) 緩動曲線
- 點綴「建築圖紙」元素：極淡方格網底紋、巨型半透明輪廓編號、帶刻度的細標註線、角落十字記號

請用上面的色票與字體，不要使用 Material Design 或 Bootstrap 的預設樣式。
```

---

## ② 色彩 Tokens

| 用途 | 名稱 | HEX | 備註 |
|---|---|---|---|
| 頁面底色 | warm-white 暖象牙白 | `#f5f3ee` | 主背景，取代純白 |
| 主文字／深色區塊 | charcoal 深炭 | `#1c1a17` | 取代純黑 |
| 品牌主色 | emerald-brand | `#064e3b` | 深綠，按鈕／重點 |
| 品牌輔色 | emerald-brand-light | `#10b981` | 亮綠，僅深底點綴 |
| 品牌極淺色 | emerald-brand-soft | `#ecfdf5` | 淺綠色塊／選取色 |

選取顏色（::selection）：底 `#064e3b` 文字 `#ecfdf5`。

---

## ③ 字體系統

| 角色 | 字體堆疊 | 典型用法 |
|---|---|---|
| 襯線標題（serif） | `Playfair Display, Noto Serif TC, serif` | H1/H2 大標、英文案名（常用 italic） |
| 無襯線內文（sans） | `Inter, Noto Sans TC, sans-serif` | 內文、按鈕 |
| 等寬（mono） | `JetBrains Mono, monospace` | 標籤、編號、英文小標（大寫＋寬字距 0.2–0.4em） |

- 中文字距：一般 `0.05em`、寬版 `0.12em`
- 標題用細字重（300/font-light）＋大字級，營造精品感
- Google Fonts 載入字串：
  `Inter:wght@200;300;400;500;600` / `Playfair Display:ital,wght@0,400;0,700;1,400` / `Noto Serif TC:wght@300..700` / `Noto Sans TC:wght@300;400;500;700` / `JetBrains Mono:wght@300`

---

## ④ 標誌性視覺效果（要在 design 裡重現這些，貼對應 CSS）

### 磨砂玻璃卡片（品牌核心元素）
```css
/* 輕量玻璃（導覽列、標籤、浮動提示） */
.glass {
  background: rgba(255,255,255,0.72);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.90);
  box-shadow: 0 2px 12px rgba(28,26,23,0.06);
}
/* 立體玻璃卡片（內容面板、表單） */
.glass-card {
  background: rgba(255,255,255,0.88);
  backdrop-filter: blur(32px) saturate(200%);
  border: 1px solid rgba(255,255,255,0.95);
  box-shadow: 0 4px 24px rgba(28,26,23,0.07),
              inset 0 1px 0 rgba(255,255,255,0.98);
}
/* hover 懸浮 */
.glass-lift { transition: transform .4s cubic-bezier(0.16,1,0.3,1), box-shadow .4s cubic-bezier(0.16,1,0.3,1); }
.glass-lift:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(28,26,23,0.12); }
/* 深色玻璃（深色 Hero 上的浮動元素） */
.glass-dark {
  background: rgba(15,14,12,0.58);
  backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid rgba(255,255,255,0.10);
}
```

### 建築圖紙設計語言（品牌專業識別）
```css
/* 圖紙方格網底紋（極淡，不搶內容） */
.blueprint-grid {
  background-image:
    linear-gradient(rgba(6,78,59,0.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(6,78,59,0.045) 1px, transparent 1px);
  background-size: 52px 52px;
}
/* 巨型輪廓編號水印（如圖紙 Sheet Number） */
.sheet-num {
  font-family: 'Playfair Display', serif;
  font-size: clamp(9rem, 22vw, 20rem); line-height: .8;
  -webkit-text-stroke: 1.5px rgba(28,26,23,0.10);
  color: transparent; position: absolute; z-index: 0;
}
/* 帶刻度的標註線（建築尺寸線感） */
.dim-line { position: relative; height: 1px; background: rgba(28,26,23,0.18); }
.dim-line::before, .dim-line::after {
  content:''; position:absolute; top:-3px; width:1px; height:7px; background: rgba(28,26,23,0.18);
}
.dim-line::before{left:0} .dim-line::after{right:0}
/* 圖紙角標：對角十字記號 */
.corner-marks::before, .corner-marks::after {
  font-family:'JetBrains Mono'; font-size:14px; color: rgba(6,78,59,0.35); position:absolute;
}
.corner-marks::before{content:'+'; top:-7px; left:-7px}
.corner-marks::after{content:'+'; bottom:-7px; right:-7px}
```

### 動效與緩動
- 通用緩動曲線：`cubic-bezier(0.16, 1, 0.3, 1)`（優雅、緩出）
- 進場：fade-in-up（位移 28px + 淡入，約 1.1s）
- Hero 大圖：slow-zoom（20s 緩慢縮放）
- 按鈕 hover：一道斜光掃過（btn-sheen）
- 翠綠光暈：`box-shadow: 0 0 24px rgba(6,78,59,0.20), 0 0 48px rgba(6,78,59,0.08);`

---

## ⑤ 版面慣例

- 容器寬度：max-width `1280px`（max-w-7xl），左右間距 `px-5`（手機）/ `px-10`（桌機）
- 區塊上下間距：`py-28`（手機）/ `py-36`（桌機）
- 行高：內文 `1.75`；標題用 `text-wrap: balance`，內文用 `text-wrap: pretty`
- 圓角：卡片常用大圓角（`rounded-2xl` ~ `rounded-[2.5rem]`）
- 圖片：常用 `grayscale` 灰階，hover 時轉為彩色（`grayscale-0`）＋ 微放大
- 捲軸：細 4px，hover 轉品牌綠

---

## ⑥ 範例語句（依場景挑用，接在開場白後面）

- 建案銷售頁：「幫我設計一個高級建案的銷售落地頁，要有深色 Hero（建築實景＋深綠標籤）、五大工法的圖文交錯區、磨砂玻璃的規格卡片、底部 CTA 預約諮詢。」
- 品牌介紹：「設計一個關於我們頁面，含品牌故事、里程碑時間軸、數字統計（用 Playfair 大數字），保持大量留白與建築圖紙網格底紋。」
- 卡片元件：「做一組建案卡片，磨砂玻璃材質、hover 懸浮、左上角用等寬字體標卷宗編號 JC-001、圖片灰階轉彩色。」

---

*資料來源：傑丞官網 `tailwind.config.js` 與 `assets/css/main.css`，數值為實際生產設定。*
