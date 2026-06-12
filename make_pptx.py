"""Generate three PPTX files from the Reveal.js presentations."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

W = Inches(13.33)   # 1280px at 96dpi
H = Inches(7.5)     # 720px

def rgb(h):
    h = h.lstrip('#')
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))

def new_prs():
    prs = Presentation()
    prs.slide_width  = W
    prs.slide_height = H
    return prs

def blank_slide(prs):
    layout = prs.slide_layouts[6]   # completely blank
    return prs.slides.add_slide(layout)

def fill_bg(slide, hex_color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = rgb(hex_color)

def txb(slide, text, left, top, width, height,
        size=18, bold=False, color='#1a1a1a', align=PP_ALIGN.LEFT,
        wrap=True, italic=False):
    tf_box = slide.shapes.add_textbox(left, top, width, height)
    tf = tf_box.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = rgb(color)
    return tf_box

def txb_lines(slide, lines, left, top, width, height,
              size=14, color='#1a1a1a', bold_first=False, bullet=False):
    """lines: list of str. bullet=True adds • prefix."""
    tf_box = slide.shapes.add_textbox(left, top, width, height)
    tf = tf_box.text_frame
    tf.word_wrap = True
    first = True
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        run = p.add_run()
        prefix = '• ' if bullet else ''
        run.text = prefix + line
        run.font.size = Pt(size)
        run.font.bold = (bold_first and first)
        run.font.color.rgb = rgb(color)
        first = False
    return tf_box

def rect(slide, left, top, width, height, hex_color):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(hex_color)
    shape.line.fill.background()
    return shape

# ─────────────────────────────────────────────
# Helper: accent bar (thin colored line)
# ─────────────────────────────────────────────
def accent_bar(slide, left, top, width, hex_color):
    rect(slide, left, top, width, Pt(3), hex_color)

# ─────────────────────────────────────────────
# EEWH presentation  (20 slides, emerald theme)
# ─────────────────────────────────────────────
EMERALD   = '#064e3b'
EMERALD_L = '#10b981'
BLUE      = '#1e40af'
BLUE_L    = '#3b82f6'
CHARCOAL  = '#1a1a1a'
GRAY      = '#6b7280'
LIGHT_BG  = '#f0fdf4'
BLUE_BG   = '#eff6ff'
WHITE     = '#ffffff'

def build_eewh(path):
    prs = new_prs()

    # ── 01 Cover ──────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl, '#1a1a1a')
    txb(sl,'傑丞建築機構 / Jieceng Architecture',
        Inches(1),Inches(.6),Inches(11),Inches(.4),
        size=13,color='#10b981')
    txb(sl,'綠建築標章',
        Inches(1),Inches(1.2),Inches(11),Inches(1),
        size=48,bold=True,color=WHITE)
    txb(sl,'2023 版解析',
        Inches(1),Inches(2.0),Inches(11),Inches(.9),
        size=40,bold=True,color='#10b981')
    rect(sl,Inches(1),Inches(3.05),Inches(.7),Pt(4),EMERALD_L)
    txb(sl,'基本型（EEWH-BC）× 住宅型（EEWH-RS）完整介紹',
        Inches(1),Inches(3.3),Inches(11),Inches(.4),
        size=16,color='#9ca3af')
    txb(sl,'暨 傑丞建築機構 永續建築專案成果',
        Inches(1),Inches(3.75),Inches(11),Inches(.4),
        size=16,color='#9ca3af')
    txb(sl,'2026.05.26',
        Inches(1),Inches(6.8),Inches(4),Inches(.4),
        size=12,color='#4b5563')

    # ── 02 Agenda ─────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl, '#fafaf9')
    accent_bar(sl,Inches(1),Inches(.8),Inches(1.2),EMERALD)
    txb(sl,'今日議程',Inches(1),Inches(1),Inches(11),Inches(.6),
        size=32,bold=True,color=CHARCOAL)
    txb(sl,'PART 01 — 綠建築 EEWH 2023',
        Inches(1),Inches(1.9),Inches(5.5),Inches(.35),
        size=13,color=EMERALD)
    txb_lines(sl,[
        '制度沿革與 2023 版更新重點','EEWH 適用類型總覽',
        '九大評估指標架構','基本型（EEWH-BC）深度介紹',
        '住宅型（EEWH-RS）深度介紹','兩型比較 × 五個認證等級'],
        Inches(1),Inches(2.3),Inches(5.5),Inches(2.5),
        size=15,color=CHARCOAL,bullet=True)
    txb(sl,'PART 02 — 傑丞建築機構',
        Inches(7),Inches(1.9),Inches(5.5),Inches(.35),
        size=13,color=EMERALD)
    txb_lines(sl,[
        '公司理念與服務','開放建築','當層配管','複層樓板','都市更新'],
        Inches(7),Inches(2.3),Inches(5.5),Inches(2.5),
        size=15,color=CHARCOAL,bullet=True)

    # ── 03 Part1 interlude ────────────────────
    sl = blank_slide(prs)
    fill_bg(sl, EMERALD)
    txb(sl,'PART 01',Inches(1),Inches(1.2),Inches(11),Inches(.4),
        size=13,color='#a7f3d0')
    txb(sl,'綠建築標章 EEWH 2023',
        Inches(1),Inches(1.8),Inches(11),Inches(1.4),
        size=44,bold=True,color=WHITE)
    rect(sl,Inches(1),Inches(3.35),Inches(.6),Pt(4),EMERALD_L)
    txb(sl,'從 1999 年開創亞熱帶綠建築標準到 2023 年配合淨零碳排路徑，\nEEWH 持續進化，為台灣建築環境品質立下新里程。',
        Inches(1),Inches(3.6),Inches(10),Inches(1),
        size=16,color='#a7f3d0')

    # ── 04 Timeline & 2023 updates ───────────
    sl = blank_slide(prs)
    fill_bg(sl, '#fafaf9')
    txb(sl,'EEWH ／ 制度沿革',Inches(1),Inches(.5),Inches(4),Inches(.4),
        size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.95),Inches(1.2),EMERALD)
    txb(sl,'從 1999 到 2023：持續進化',
        Inches(1),Inches(1.1),Inches(11),Inches(.6),
        size=28,bold=True,color=CHARCOAL)
    # timeline dots
    years=[('1999','EEWH 創立\n全球首個亞熱帶標章'),
           ('2007','九大指標系統確立'),
           ('2015','多類型版本正式推行'),
           ('2022','配合 BERS 系統銜接'),
           ('2023★','淨零路徑版本更新')]
    for i,(yr,desc) in enumerate(years):
        x = Inches(1+i*2.3)
        c = EMERALD_L if '★' in yr else '#6b7280'
        rect(sl,x,Inches(2.0),Inches(.55),Inches(.55),c)
        txb(sl,yr.replace('★',''),x,Inches(2.0),Inches(.55),Inches(.55),
            size=11,bold=True,color=WHITE,align=PP_ALIGN.CENTER)
        txb(sl,yr,x-Inches(.1),Inches(2.65),Inches(.8),Inches(.3),
            size=11,bold=('★' in yr),color=EMERALD_L if '★' in yr else CHARCOAL)
        txb(sl,desc,x-Inches(.15),Inches(2.95),Inches(.9),Inches(.8),
            size=10,color=GRAY)
    txb(sl,'2023 版五大更新重點',
        Inches(1),Inches(3.85),Inches(11),Inches(.4),
        size=16,bold=True,color=CHARCOAL)
    updates=[
        ('① 節能門檻提升','ENVLOAD 要求更嚴格，與 BERS 第 3 級以上銜接'),
        ('② 碳排生命週期評估','CO₂ 減量指標納入建材 LCA，評估延伸至全生命週期'),
        ('③ PM2.5 空氣品質','室內環境新增 PM2.5 ≤ 35 μg/m³ 監測要求'),
        ('④ 生態廊道加分','生物多樣性指標新增生態廊道設計加分項'),
    ]
    for i,(title,desc) in enumerate(updates):
        col = i%2; row = i//2
        bx = Inches(1+col*6.1)
        by = Inches(4.3+row*1.4)
        rect(sl,bx,by,Inches(5.8),Inches(1.25),'#f0fdf4')
        txb(sl,title,bx+Inches(.15),by+Inches(.1),Inches(5.5),Inches(.35),
            size=13,bold=True,color=EMERALD)
        txb(sl,desc,bx+Inches(.15),by+Inches(.45),Inches(5.5),Inches(.65),
            size=11,color=CHARCOAL)

    # ── 05 五種類型 ──────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'EEWH ／ 適用類型',Inches(1),Inches(.5),Inches(4),Inches(.4),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.95),Inches(1.2),EMERALD)
    txb(sl,'五種評估版本，本次聚焦兩型',
        Inches(1),Inches(1.1),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    types=[
        ('EEWH-BC','基本型','辦公、商業、學校、醫院、政府機關等非住宅建築','★ 本次重點',BLUE_BG,BLUE),
        ('EEWH-RS','住宅型','集合住宅（公寓大廈）、透天住宅等居住類建築','★ 本次重點',LIGHT_BG,EMERALD),
        ('EEWH-RN','舊建改善型','既有建築節能改善、綠化補強，鼓勵老屋升級','',   '#f9fafb','#6b7280'),
        ('EEWH-NC','社區型',  '社區整體環境與共用設施的綠化評估','',              '#f9fafb','#6b7280'),
        ('EEWH-OF','廠房型',  '工廠、倉儲、廠辦等工業性質建築','',               '#f9fafb','#6b7280'),
    ]
    cols=[0,1,2,0,1]
    rows=[0,0,0,1,1]
    for i,(code,name,desc,badge,bg,fc) in enumerate(types):
        col=cols[i]; row=rows[i]
        bx=Inches(1+col*4.1); by=Inches(2.0+row*2.3)
        rect(sl,bx,by,Inches(3.9),Inches(2.1),bg)
        txb(sl,code,bx+Inches(.12),by+Inches(.1),Inches(3.6),Inches(.3),size=11,color=fc)
        txb(sl,name,bx+Inches(.12),by+Inches(.4),Inches(3.6),Inches(.4),size=18,bold=True,color=fc)
        txb(sl,desc,bx+Inches(.12),by+Inches(.82),Inches(3.6),Inches(.7),size=11,color=CHARCOAL)
        if badge:
            txb(sl,badge,bx+Inches(.12),by+Inches(1.65),Inches(3.6),Inches(.3),size=11,bold=True,color=fc)

    # ── 06 九大指標 ──────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'EEWH ／ 評估架構',Inches(1),Inches(.4),Inches(4),Inches(.35),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.78),Inches(1.2),EMERALD)
    txb(sl,'九大指標 — 共用架構',
        Inches(1),Inches(.9),Inches(11),Inches(.55),size=28,bold=True,color=CHARCOAL)
    cats=[
        ('生態類 Ecology', ['01 生物多樣性 — 生態棲地與物種保育',
                            '02 綠化量 — 植栽固碳效果',
                            '03 基地保水 — 雨水入滲與滯洪'],'#f0fdf4',EMERALD),
        ('節能類 Energy Saving',['04 ★ 日常節能（必要）— ENVLOAD × 空調效率 × 照明效率'],'#eff6ff',BLUE),
        ('減廢類 Waste Reduction',['05 CO₂ 減量 — 建材生命週期碳排（2023新增LCA）',
                                   '06 廢棄物減量 — 施工廢料分類管控'],'#fffbeb','#b45309'),
        ('健康類 Health',['07 ★ 室內環境（必要）— 採光、通風、PM2.5',
                          '08 ★ 水資源（必要）— 節水設備與回收利用',
                          '09 ★ 污水垃圾（必要）— 廢棄物處理設施'],'#fdf4ff','#7c3aed'),
    ]
    y=Inches(1.55)
    for cat,items,bg,fc in cats:
        rect(sl,Inches(1),y,Inches(11.3),Inches(.32),fc)
        txb(sl,cat,Inches(1.1),y+Pt(2),Inches(11),Inches(.28),size=12,bold=True,color=WHITE)
        y+=Inches(.35)
        for item in items:
            rect(sl,Inches(1),y,Inches(11.3),Inches(.38),bg)
            txb(sl,item,Inches(1.2),y+Pt(3),Inches(11),Inches(.32),size=12,color=CHARCOAL)
            y+=Inches(.4)
        y+=Inches(.05)
    txb(sl,'★ 必要指標：所有類型均需全數通過，方可進入評分',
        Inches(1),Inches(7.0),Inches(11),Inches(.35),size=11,color=GRAY,italic=True)

    # ── 07 EEWH-BC 概述 ──────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'基本型 EEWH-BC',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=BLUE)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),BLUE_L)
    txb(sl,'基本型 — 商業・辦公・公共建築',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    txb(sl,'基本型（EEWH-BC）適用於學校、辦公、商業、醫院、政府機關等各類非住宅建築，\n是台灣使用最廣泛的綠建築評估版本，側重建築系統整體性能的提升。',
        Inches(1),Inches(1.8),Inches(6.5),Inches(1.2),size=14,color=CHARCOAL)
    # stats
    for i,(num,lbl) in enumerate([('4','必要指標'),('9','評估指標')]):
        bx=Inches(1+i*1.8)
        txb(sl,num,bx,Inches(3.1),Inches(1.6),Inches(.7),size=36,bold=True,color=EMERALD)
        txb(sl,lbl,bx,Inches(3.8),Inches(1.6),Inches(.35),size=12,color=GRAY)
    txb(sl,'強制申請門檻',Inches(1),Inches(4.3),Inches(5),Inches(.35),size=13,bold=True,color=CHARCOAL)
    txb_lines(sl,['公有建築：樓地板面積 ≥ 500 m²','私有建築：依各縣市自治條例'],
        Inches(1),Inches(4.7),Inches(5.5),Inches(.8),size=12,color=CHARCOAL,bullet=True)
    # right card
    rect(sl,Inches(7.5),Inches(1.8),Inches(5),Inches(2.0),BLUE_BG)
    txb(sl,'適用建築類型',Inches(7.65),Inches(1.9),Inches(4.7),Inches(.35),size=13,bold=True,color=BLUE)
    txb_lines(sl,['辦公大樓','商業建築','學校教育','醫療院所','政府機關','旅館飯店'],
        Inches(7.65),Inches(2.3),Inches(4.7),Inches(1.3),size=12,color=CHARCOAL,bullet=True)
    rect(sl,Inches(7.5),Inches(3.95),Inches(5),Inches(1.9),BLUE_BG)
    txb(sl,'評估核心精神',Inches(7.65),Inches(4.05),Inches(4.7),Inches(.35),size=13,bold=True,color=BLUE)
    txb_lines(sl,['建築系統整體能源效率','空調 × 照明 × 外殼節能三軸並進','建材碳排與廢料管控','基地生態環境品質提升'],
        Inches(7.65),Inches(4.45),Inches(4.7),Inches(1.2),size=12,color=CHARCOAL,bullet=True)

    # ── 08 EEWH-BC 評估重點 ──────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'基本型 EEWH-BC ／ 評估重點',Inches(1),Inches(.5),Inches(6),Inches(.4),size=12,color=BLUE)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),BLUE_L)
    txb(sl,'基本型四大評估核心',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    cards_bc=[
        ('① 日常節能（必要）',
         ['外殼耗能 ENVLOAD 優於基準 15%（2023版）',
          '空調效率 COP / EER 達省能標準',
          '照明功率密度 LPD 符合規範']),
        ('② 水資源（必要）',
         ['全棟節水器具省水率 ≥ 20%',
          '屋頂雨水回收 × 空調冷凝水利用',
          '中水回收系統（免治馬桶／沖廁）',
          '自動澆灌節水設計']),
        ('③ CO₂ 減量（選擇）',
         ['主結構（RC / 鋼構）選材',
          '建材隱含碳排放量計算',
          '在地建材 × 低碳建材優先使用',
          '生命週期碳排 LCA 報告（2023新增加分）']),
        ('④ 室內環境（必要）',
         ['採光：辦公空間照度達標',
          '通風：換氣次數符合規範',
          '音環境：隔音量 STC 基準',
          'PM2.5 ≤ 35 μg/m³（2023版新增）']),
    ]
    for i,(title,items) in enumerate(cards_bc):
        col=i%2; row=i//2
        bx=Inches(1+col*6.1); by=Inches(2.0+row*2.5)
        rect(sl,bx,by,Inches(5.8),Inches(2.35),BLUE_BG)
        txb(sl,title,bx+Inches(.15),by+Inches(.1),Inches(5.5),Inches(.4),size=14,bold=True,color=BLUE)
        txb_lines(sl,items,bx+Inches(.15),by+Inches(.55),Inches(5.5),Inches(1.7),size=12,color=CHARCOAL,bullet=True)

    # ── 09 EEWH-RS 概述 ──────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'住宅型 EEWH-RS',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),EMERALD)
    txb(sl,'住宅型 — 以居住者健康為核心',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    txb(sl,'住宅型（EEWH-RS）專門針對集合住宅及透天住宅設計，更強調健康舒適的生活環境、\n外殼節能設計及以居住單元為基礎的細緻評估。',
        Inches(1),Inches(1.8),Inches(6.5),Inches(1.2),size=14,color=CHARCOAL)
    for i,(num,lbl) in enumerate([('4','必要指標'),('24h','全天居住使用')]):
        bx=Inches(1+i*2.4)
        txb(sl,num,bx,Inches(3.1),Inches(2.2),Inches(.7),size=32,bold=True,color=EMERALD)
        txb(sl,lbl,bx,Inches(3.8),Inches(2.2),Inches(.35),size=12,color=GRAY)
    txb(sl,'強制申請門檻',Inches(1),Inches(4.3),Inches(5),Inches(.35),size=13,bold=True,color=CHARCOAL)
    txb_lines(sl,['集合住宅：戶數 ≥ 30 戶','社區型集合住宅：基地面積 ≥ 3,000 m²'],
        Inches(1),Inches(4.7),Inches(5.5),Inches(.8),size=12,color=CHARCOAL,bullet=True)
    rect(sl,Inches(7.5),Inches(1.8),Inches(5),Inches(2.0),LIGHT_BG)
    txb(sl,'適用建築類型',Inches(7.65),Inches(1.9),Inches(4.7),Inches(.35),size=13,bold=True,color=EMERALD)
    txb_lines(sl,['集合住宅','公寓大廈','透天住宅','社區住宅','出租住宅','社會住宅'],
        Inches(7.65),Inches(2.3),Inches(4.7),Inches(1.3),size=12,color=CHARCOAL,bullet=True)
    rect(sl,Inches(7.5),Inches(3.95),Inches(5),Inches(1.9),LIGHT_BG)
    txb(sl,'住宅型核心精神',Inches(7.65),Inches(4.05),Inches(4.7),Inches(.35),size=13,bold=True,color=EMERALD)
    txb_lines(sl,['全天使用 → 外殼節能更嚴格','居住健康 → 室內環境細化評估','以戶計量 → 住戶節水獨立計量','社區生態 → 基地共用綠化空間'],
        Inches(7.65),Inches(4.45),Inches(4.7),Inches(1.2),size=12,color=CHARCOAL,bullet=True)

    # ── 10 EEWH-RS 評估重點 ──────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'住宅型 EEWH-RS ／ 評估重點',Inches(1),Inches(.5),Inches(6),Inches(.4),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),EMERALD)
    txb(sl,'住宅型四大評估核心',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    cards_rs=[
        ('① 日常節能（必要）',
         ['外牆熱傳透率 U 值更嚴（較基本型提高 10%）',
          '頂層樓板或屋頂遮陽隔熱設計',
          '窗牆比控制 × 遮陽板 × Low-E 玻璃']),
        ('② 水資源（必要）',
         ['每戶獨立水表計量（提高節水意識）',
          '省水標章馬桶、水龍頭、蓮蓬頭',
          '雨水回收 → 社區庭院澆灌',
          '省水率整體 ≥ 20%']),
        ('③ 室內環境（必要）',
         ['採光：主要居室採光係數 ≥ 0.03',
          '通風：自然通風開口比 ≥ 1/8 樓地板面積',
          '隔音：樓板衝擊音 ≤ 58 dB（比辦公更嚴格）',
          'PM2.5：≤ 35 μg/m³ 年均值（2023新增）']),
        ('④ 生態指標（選擇）',
         ['社區庭院 × 頂樓花園綠化量',
          '基地保水：透水鋪面 × 雨水花園',
          '生物多樣性：蟲鳥棲地植栽選種',
          '生態廊道銜接設計（2023新增加分）']),
    ]
    for i,(title,items) in enumerate(cards_rs):
        col=i%2; row=i//2
        bx=Inches(1+col*6.1); by=Inches(2.0+row*2.5)
        rect(sl,bx,by,Inches(5.8),Inches(2.35),LIGHT_BG)
        txb(sl,title,bx+Inches(.15),by+Inches(.1),Inches(5.5),Inches(.4),size=14,bold=True,color=EMERALD)
        txb_lines(sl,items,bx+Inches(.15),by+Inches(.55),Inches(5.5),Inches(1.7),size=12,color=CHARCOAL,bullet=True)

    # ── 11 BC vs RS 比較 ─────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'綜合比較',Inches(1),Inches(.5),Inches(4),Inches(.4),size=12,color=GRAY)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),CHARCOAL)
    txb(sl,'基本型 vs 住宅型 — 差異對照',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    rows_data=[
        ('適用建築','辦公、商業、學校、醫院、公共設施','集合住宅、公寓大廈、透天住宅'),
        ('使用情境','日間為主（8–10 小時）','全天 24 小時居住使用'),
        ('節能重點','空調系統效率 COP/EER 為主','外殼隔熱設計（外牆 U 值更嚴格）'),
        ('水資源','系統性節水設備、中水回收','每戶獨立水表計量＋省水標章'),
        ('室內環境','工作場域：照度、通風、音環境','居住健康：採光係數、自然通風、樓板隔音'),
        ('生態指標','基地生態與景觀綠化','社區共用庭院、頂樓綠化、生態廊道'),
        ('強制對象','公有建築 ≥ 500 m²','集合住宅 ≥ 30 戶'),
        ('評估單位','整棟建築系統','整棟 + 各居住單元細分'),
    ]
    # header
    rect(sl,Inches(1),Inches(1.85),Inches(2.5),Inches(.42),CHARCOAL)
    txb(sl,'比較項目',Inches(1.05),Inches(1.88),Inches(2.4),Inches(.38),size=12,bold=True,color=WHITE)
    rect(sl,Inches(3.55),Inches(1.85),Inches(4.5),Inches(.42),BLUE)
    txb(sl,'基本型 EEWH-BC',Inches(3.6),Inches(1.88),Inches(4.4),Inches(.38),size=12,bold=True,color=WHITE)
    rect(sl,Inches(8.1),Inches(1.85),Inches(4.5),Inches(.42),EMERALD)
    txb(sl,'住宅型 EEWH-RS',Inches(8.15),Inches(1.88),Inches(4.4),Inches(.38),size=12,bold=True,color=WHITE)
    for i,(rh,bc,rs) in enumerate(rows_data):
        bg='#f9fafb' if i%2==0 else WHITE
        y=Inches(2.35+i*.6)
        rect(sl,Inches(1),y,Inches(2.5),Inches(.55),bg)
        rect(sl,Inches(3.55),y,Inches(4.5),Inches(.55),bg)
        rect(sl,Inches(8.1),y,Inches(4.5),Inches(.55),bg)
        txb(sl,rh,Inches(1.05),y+Pt(3),Inches(2.4),Inches(.48),size=11,bold=True,color=CHARCOAL)
        txb(sl,bc,Inches(3.6),y+Pt(3),Inches(4.4),Inches(.48),size=11,color=CHARCOAL)
        txb(sl,rs,Inches(8.15),y+Pt(3),Inches(4.4),Inches(.48),size=11,color=CHARCOAL)

    # ── 12 五個認證等級 ──────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'EEWH ／ 認證等級',Inches(1),Inches(.5),Inches(4),Inches(.4),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),EMERALD)
    txb(sl,'五個認證等級 — 基本型 × 住宅型共用',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    levels=[
        ('🌿','合格級','Qualified','基礎門檻','#6b7280'),
        ('🥉','銅　級','Bronze',  '良好表現','#92400e'),
        ('🥈','銀　級','Silver',  '優良表現','#64748b'),
        ('🥇','黃金級','Gold',    '卓越表現','#b45309'),
        ('💎','鑽石級','Diamond', '頂尖典範','#1e40af'),
    ]
    for i,(icon,name,en,score,fc) in enumerate(levels):
        bx=Inches(1+i*2.35)
        rect(sl,bx,Inches(1.85),Inches(2.15),Inches(2.5),'#f9fafb')
        txb(sl,icon,bx,Inches(1.95),Inches(2.15),Inches(.6),
            size=28,align=PP_ALIGN.CENTER)
        txb(sl,name,bx,Inches(2.65),Inches(2.15),Inches(.4),
            size=15,bold=True,color=fc,align=PP_ALIGN.CENTER)
        txb(sl,en,  bx,Inches(3.05),Inches(2.15),Inches(.3),
            size=11,color=GRAY,align=PP_ALIGN.CENTER)
        txb(sl,score,bx,Inches(3.35),Inches(2.15),Inches(.3),
            size=12,bold=True,color=fc,align=PP_ALIGN.CENTER)
    txb(sl,'評分邏輯',Inches(1),Inches(4.6),Inches(11),Inches(.4),size=16,bold=True,color=CHARCOAL)
    rect(sl,Inches(1),Inches(5.05),Inches(5.8),Inches(1.7),'#f9fafb')
    txb(sl,'通過條件',Inches(1.15),Inches(5.15),Inches(5.5),Inches(.35),size=13,bold=True,color=CHARCOAL)
    txb_lines(sl,['4 項必要指標全數通過','選擇指標累計得分達等級門檻','基本型與住宅型分開計算基準值'],
        Inches(1.15),Inches(5.55),Inches(5.5),Inches(1.0),size=12,color=CHARCOAL,bullet=True)
    rect(sl,Inches(7.1),Inches(5.05),Inches(5.5),Inches(1.7),'#f9fafb')
    txb(sl,'有效期限',Inches(7.25),Inches(5.15),Inches(5.2),Inches(.35),size=13,bold=True,color=CHARCOAL)
    txb_lines(sl,['標章有效期 5 年','到期前需重新評定或展延','建築改善後可申請升級評定'],
        Inches(7.25),Inches(5.55),Inches(5.2),Inches(1.0),size=12,color=CHARCOAL,bullet=True)

    # ── 13 申請流程 ──────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'EEWH ／ 申請程序',Inches(1),Inches(.5),Inches(4),Inches(.4),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),EMERALD)
    txb(sl,'申請流程（基本型 × 住宅型相同）',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    steps=[
        ('STEP 01','📋','設計階段\n申請候選','取得「候選綠建築證書」，確認設計方向符合評估需求'),
        ('STEP 02','🏗️','施工期間\n文件蒐集','建材採購單、施工照片、節水設備規格書等文件備齊'),
        ('STEP 03','✅','竣工後\n正式評定','向建研所申請書面審查＋現場勘查，核發正式標章'),
    ]
    for i,(num,icon,title,desc) in enumerate(steps):
        bx=Inches(1+i*4.1)
        rect(sl,bx,Inches(2.0),Inches(3.8),Inches(2.5),'#f0fdf4')
        txb(sl,num, bx+Inches(.15),Inches(2.1),Inches(3.5),Inches(.3),size=11,color=EMERALD)
        txb(sl,icon,bx+Inches(.15),Inches(2.42),Inches(3.5),Inches(.45),size=22)
        txb(sl,title,bx+Inches(.15),Inches(2.95),Inches(3.5),Inches(.55),size=14,bold=True,color=CHARCOAL)
        txb(sl,desc, bx+Inches(.15),Inches(3.55),Inches(3.5),Inches(.8),size=11,color=GRAY)
        if i<2:
            txb(sl,'→',Inches(4.85+i*4.1),Inches(3.0),Inches(.4),Inches(.4),size=18,color=GRAY)
    txb(sl,'基本型申請注意事項',Inches(1),Inches(4.85),Inches(5.5),Inches(.35),size=13,bold=True,color=BLUE)
    txb_lines(sl,['空調系統須有機電技師簽證','照明計算需附設計圖說','建材碳排計算表格（2023版新增）'],
        Inches(1),Inches(5.25),Inches(5.5),Inches(.9),size=12,color=CHARCOAL,bullet=True)
    txb(sl,'住宅型申請注意事項',Inches(7),Inches(4.85),Inches(5.5),Inches(.35),size=13,bold=True,color=EMERALD)
    txb_lines(sl,['須附每戶水表配置圖','隔音工程需有施工說明書','頂樓/外牆隔熱材料規格文件'],
        Inches(7),Inches(5.25),Inches(5.5),Inches(.9),size=12,color=CHARCOAL,bullet=True)

    # ── 14 Part2 interlude ───────────────────
    sl = blank_slide(prs)
    fill_bg(sl,EMERALD)
    txb(sl,'PART 02',Inches(1),Inches(1.2),Inches(11),Inches(.4),size=13,color='#a7f3d0')
    txb(sl,'傑丞建築機構\n專案成果',
        Inches(1),Inches(1.8),Inches(11),Inches(1.8),
        size=44,bold=True,color=WHITE)
    rect(sl,Inches(1),Inches(3.7),Inches(.6),Pt(4),EMERALD_L)
    txb(sl,'以 EEWH 精神為設計基底，將開放建築、SI 工法、節能外殼設計融入每一個空間，\n打造符合永續標準的居住與商業環境。',
        Inches(1),Inches(3.9),Inches(10),Inches(1),size=16,color='#a7f3d0')

    # ── 15 公司簡介 ──────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'傑丞建築機構',Inches(1),Inches(.5),Inches(4),Inches(.4),size=12,color=EMERALD)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),EMERALD)
    txb(sl,'理念 · 工法 · 空間美學',
        Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    txb(sl,'傑丞建築機構以極簡留白與優雅動態傳遞品牌的專業工法與空間美學，\n致力於將最新建築技術融入人性化設計，打造能隨時間進化的永續居住環境。',
        Inches(1),Inches(1.8),Inches(6.5),Inches(1.2),size=14,color=CHARCOAL)
    txb_lines(sl,['開放建築（Open Building）專利應用','SI 管線分離工法（當層配管）','全案管理 PCM 顧問服務','EEWH 住宅型永續設計規劃'],
        Inches(1),Inches(3.1),Inches(6.5),Inches(1.6),size=13,color=CHARCOAL,bullet=True)
    stats2=[('4+','代表作品'),('PCM','全案管理服務'),('SI','管線分離工法'),('EEWH','綠建築設計導入')]
    for i,(num,lbl) in enumerate(stats2):
        col=i%2; row=i//2
        bx=Inches(8.1+col*2.3); by=Inches(1.8+row*2.3)
        bg=LIGHT_BG if i==3 else '#f9fafb'
        rect(sl,bx,by,Inches(2.1),Inches(2.0),bg)
        txb(sl,num,bx,by+Inches(.3),Inches(2.1),Inches(.9),size=28,bold=True,color=EMERALD,align=PP_ALIGN.CENTER)
        txb(sl,lbl,bx,by+Inches(1.2),Inches(2.1),Inches(.4),size=11,color=GRAY,align=PP_ALIGN.CENTER)

    # ── 16-19 Projects ───────────────────────
    projects=[
        ('開放建築',   'Residential ／ 台北市 信義區 ／ 2024',
         '利用自然採光與極簡線條，打造開放式居住空間。採用可變動的彈性隔間技術，\n讓住戶能隨著生命週期的變化，自由調整室內佈局。',
         '台北市 信義區','2024','120 sqm',
         ['EEWH-RS 住宅型','Open Building Patent'],
         '彈性隔間設計降低裝修碳排，延長建物使用壽命，\n契合 EEWH-RS CO₂ 減量及室內環境指標精神。',EMERALD,LIGHT_BG),
        ('當層配管',   'Commercial ／ 新北市 板橋區 ／ 2023',
         '引進當層配管專利技術，解決傳統建築漏水難以維修的痛點，\n實現管線與結構體徹底分離，大幅提升建物壽命，並結合工業風格與綠色植物。',
         '新北市 板橋區','2023','450 sqm',
         ['EEWH-BC 基本型','SI Separation'],
         'SI 工法將管線獨立於當層樓板，維修不擾鄰，\n對應 EEWH-BC 水資源指標中的管路維護效益。',BLUE_L,BLUE_BG),
        ('複層樓板',   'Landscape ／ 台中市 西屯區 ／ 2024',
         '透過複層樓板設計創造出極佳的隔音效果與微氣候調節空間，\n強調人與自然互動，讓室內環境不受外界噪音干擾，維持恆溫舒適。',
         '台中市 西屯區','2024','800 sqm',
         ['EEWH-RS 住宅型','Double-Layer Floor'],
         '空氣層設計同步達到隔音（≤ 58 dB）、隔熱、管線整合三重效益，\n完整呼應 EEWH-RS 室內環境指標樓板隔音要求。',EMERALD,LIGHT_BG),
        ('都市更新',   'Renovation ／ 台北市 大同區 ／ 2023',
         '保留歷史紋理，注入現代機能，賦予老建築新生命。\n在尊重原有結構與街區記憶的前提下，導入現代化機能與安全規範。',
         '台北市 大同區','2023','320 sqm',
         ['EEWH-RN 舊建改善型','Urban Renewal'],
         '都市更新結合 EEWH-RN 申請，在保存原有結構的前提下\n導入節能外窗、節水器具，降低整體碳排放。','#d97706','#fffbeb'),
    ]
    for title,tag,desc,loc,yr,area,badges,quote,ac,bg in projects:
        sl = blank_slide(prs)
        fill_bg(sl,'#fafaf9')
        txb(sl,tag,Inches(1),Inches(.5),Inches(11),Inches(.4),size=12,color=GRAY)
        accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),ac)
        txb(sl,title,Inches(1),Inches(1.07),Inches(11),Inches(.7),size=34,bold=True,color=CHARCOAL)
        rect(sl,Inches(1),Inches(1.9),Inches(2.5),Inches(2.2),bg)
        txb(sl,'🏠',Inches(1.7),Inches(2.3),Inches(1.1),Inches(.9),size=40,align=PP_ALIGN.CENTER)
        txb(sl,desc,Inches(3.8),Inches(1.9),Inches(8.8),Inches(1.1),size=13,color=CHARCOAL)
        for j,(k,v) in enumerate([('地點',loc),('完工年',yr),('面積',area)]):
            bx=Inches(3.8+j*3.0)
            txb(sl,k,bx,Inches(3.15),Inches(2.8),Inches(.3),size=11,color=GRAY)
            txb(sl,v,bx,Inches(3.45),Inches(2.8),Inches(.35),size=13,bold=True,color=CHARCOAL)
        badge_txt=' | '.join(badges)
        txb(sl,badge_txt,Inches(3.8),Inches(4.0),Inches(8.8),Inches(.35),size=12,bold=True,color=ac)
        rect(sl,Inches(1),Inches(4.5),Inches(11.3),Inches(1.2),'#f0fdf4')
        txb(sl,quote,Inches(1.2),Inches(4.62),Inches(11),Inches(1.0),size=12,color='#065f46')

    # ── 20 結語 ──────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#1a1a1a')
    txb(sl,'傑丞建築機構',Inches(1),Inches(.8),Inches(10),Inches(.4),size=13,color=EMERALD_L)
    txb(sl,'以標準為基石，',Inches(1),Inches(1.4),Inches(11),Inches(.8),size=40,bold=True,color=WHITE)
    txb(sl,'以設計為靈魂',Inches(1),Inches(2.2),Inches(11),Inches(.8),size=40,bold=True,color=EMERALD_L)
    rect(sl,Inches(1),Inches(3.15),Inches(.7),Pt(4),EMERALD_L)
    txb(sl,'EEWH 2023 版的更新，代表台灣建築走向更高標準的永續未來。\n傑丞建築機構將持續以開放工法與人本設計，協助每一個建築專案取得綠建築認證，\n為居住者打造值得傳承的健康空間。',
        Inches(1),Inches(3.4),Inches(10),Inches(1.5),size=16,color='#9ca3af')
    txb(sl,'Website',Inches(1),Inches(5.5),Inches(4),Inches(.3),size=11,color=GRAY)
    txb(sl,'jeremy0819.github.io/jieceng-web',
        Inches(1),Inches(5.85),Inches(6),Inches(.35),size=13,color='#e5e7eb')
    txb(sl,'Service',Inches(1),Inches(6.3),Inches(4),Inches(.3),size=11,color=GRAY)
    txb(sl,'建築設計 ／ PCM 全案管理 ／ EEWH 綠建築顧問',
        Inches(1),Inches(6.65),Inches(8),Inches(.35),size=13,color='#e5e7eb')

    prs.save(path)
    print(f'Saved {path}')

build_eewh('/home/user/jieceng-web/presentation-EEWH.pptx')
print('EEWH done')
