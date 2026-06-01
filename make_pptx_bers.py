"""Generate BERS PPTX."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

W = Inches(13.33)
H = Inches(7.5)

def rgb(h):
    h = h.lstrip('#')
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))

def new_prs():
    prs = Presentation()
    prs.slide_width  = W
    prs.slide_height = H
    return prs

def blank_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def fill_bg(slide, hex_color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = rgb(hex_color)

def txb(slide, text, left, top, width, height,
        size=18, bold=False, color='#1a1a1a', align=PP_ALIGN.LEFT, italic=False):
    tf_box = slide.shapes.add_textbox(left, top, width, height)
    tf = tf_box.text_frame
    tf.word_wrap = True
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
              size=14, color='#1a1a1a', bullet=False):
    tf_box = slide.shapes.add_textbox(left, top, width, height)
    tf = tf_box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        run = p.add_run()
        run.text = ('• ' if bullet else '') + line
        run.font.size = Pt(size)
        run.font.color.rgb = rgb(color)
    return tf_box

def rect(slide, left, top, width, height, hex_color):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(hex_color)
    shape.line.fill.background()
    return shape

def accent_bar(slide, left, top, width, hex_color):
    rect(slide, left, top, width, Pt(3), hex_color)

STONE    = '#1c1917'
AMBER    = '#b45309'
AMBER_L  = '#d97706'
AMBER_LG = '#fbbf24'
AMBER_BG = '#fef3c7'
AMBER_XP = '#fffbeb'
CHARCOAL = '#1a1a1a'
WHITE    = '#ffffff'
GRAY     = '#6b7280'

# Energy level colors
G_1PLUS = '#14532d'  # dark green
G_1     = '#166534'
G_2     = '#15803d'
G_3     = '#65a30d'
G_4     = '#ca8a04'
G_5     = '#ea580c'
G_6     = '#dc2626'
G_7     = '#991b1b'

def build_bers(path):
    prs = new_prs()

    # ── 01 Cover ──────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl, STONE)
    txb(sl,'內政部 / 建築能效評估標示制度',
        Inches(1),Inches(.6),Inches(11),Inches(.4),size=13,color=AMBER_LG)
    txb(sl,'建築能效評估標示',
        Inches(1),Inches(1.2),Inches(11),Inches(1.0),size=44,bold=True,color=WHITE)
    txb(sl,'BERS 2024 版解析',
        Inches(1),Inches(2.1),Inches(11),Inches(.9),size=38,bold=True,color=AMBER_LG)
    rect(sl,Inches(1),Inches(3.15),Inches(.7),Pt(4),AMBER_LG)
    txb(sl,'Building Energy-efficiency Rating System',
        Inches(1),Inches(3.35),Inches(11),Inches(.4),size=15,color='#a8a29e')
    txb(sl,'EUI 能源使用強度 × 八個能效等級 × 2050 淨零建築路徑',
        Inches(1),Inches(3.78),Inches(11),Inches(.4),size=15,color='#a8a29e')
    txb(sl,'2026.05.26',Inches(1),Inches(6.8),Inches(4),Inches(.4),size=12,color='#44403c')

    # ── 02 目錄 ────────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    accent_bar(sl,Inches(1),Inches(.8),Inches(1.2),AMBER)
    txb(sl,'今日議程',Inches(1),Inches(1.0),Inches(11),Inches(.6),size=32,bold=True,color=CHARCOAL)
    txb(sl,'PART 01 — 制度與核心',Inches(1),Inches(1.85),Inches(5.5),Inches(.35),size=13,color=AMBER)
    txb_lines(sl,['什麼是 BERS？制度背景','2024 版更新重點','核心概念：EUI 能源使用強度','評估方法與節能率'],
        Inches(1),Inches(2.25),Inches(5.5),Inches(1.8),size=15,color=CHARCOAL,bullet=True)
    txb(sl,'PART 02 — 等級與應用',Inches(7),Inches(1.85),Inches(5.5),Inches(.35),size=13,color=AMBER)
    txb_lines(sl,['八個能效等級','BERS vs BERSh（一般 / 住宅）','評估系統範圍',
                   '與綠建築、智慧建築的關係','淨零路徑 × 申請流程'],
        Inches(7),Inches(2.25),Inches(5.5),Inches(2.4),size=15,color=CHARCOAL,bullet=True)

    # ── 03 制度背景 ────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 制度背景',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'為什麼需要建築能效標示？',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    txb(sl,'建築部門佔台灣總能源消費約三成，是淨零碳排的關鍵戰場。建築能效評估標示（BERS）由內政部推動，\n如同冷氣、冰箱的能源效率分級，讓建築物的能源表現可量化、可比較、可揭示，引導市場走向節能建築。',
        Inches(1),Inches(1.8),Inches(6.8),Inches(1.4),size=14,color=CHARCOAL)
    txb(sl,'三大政策目的',Inches(1),Inches(3.3),Inches(6),Inches(.35),size=13,bold=True,color=CHARCOAL)
    txb_lines(sl,['建立建築能效的客觀評比基準','揭示能效資訊，保障消費者知情權','銜接 2050 淨零碳排國家路徑'],
        Inches(1),Inches(3.7),Inches(6.5),Inches(1.0),size=13,color=CHARCOAL,bullet=True)
    # timeline (vertical)
    tl=[('2021','制度試行，建立評估方法學','#6b7280'),
        ('2022','正式推動，鼓勵自願申請','#6b7280'),
        ('2023','住宅版 BERSh 完善上線','#6b7280'),
        ('2024★','公有新建強制申請',AMBER_LG)]
    for i,(yr,desc,fc) in enumerate(tl):
        bx=Inches(8.5); by=Inches(1.8+i*1.2)
        rect(sl,bx,by,Inches(.6),Inches(.6),fc)
        txb(sl,yr.replace('★',''),bx,by,Inches(.6),Inches(.6),
            size=11,bold=True,color=WHITE if '★' not in yr else CHARCOAL,align=PP_ALIGN.CENTER)
        txb(sl,yr,bx+Inches(.7),by,Inches(1.2),Inches(.3),
            size=11,bold=('★' in yr),color=AMBER if '★' in yr else CHARCOAL)
        txb(sl,desc,bx+Inches(.7),by+Inches(.3),Inches(3.5),Inches(.5),size=11,color=GRAY)
    rect(sl,Inches(1),Inches(4.85),Inches(2.2),Inches(1.5),AMBER_BG)
    txb(sl,'~30%',Inches(1),Inches(4.95),Inches(2.2),Inches(.7),size=28,bold=True,color=AMBER,align=PP_ALIGN.CENTER)
    txb(sl,'建築佔全國能耗',Inches(1),Inches(5.65),Inches(2.2),Inches(.35),size=11,color=GRAY,align=PP_ALIGN.CENTER)
    rect(sl,Inches(3.4),Inches(4.85),Inches(2.2),Inches(1.5),AMBER_XP)
    txb(sl,'8',Inches(3.4),Inches(4.95),Inches(2.2),Inches(.7),size=40,bold=True,color=AMBER,align=PP_ALIGN.CENTER)
    txb(sl,'能效等級',Inches(3.4),Inches(5.65),Inches(2.2),Inches(.35),size=11,color=GRAY,align=PP_ALIGN.CENTER)

    # ── 04 2024 更新重點 ────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'2024 版 ／ 修訂重點',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'2024 版六大更新重點',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    updates=[
        ('① 強制範圍','公有新建建築強制申請\n新建公有建築正式納入強制申請對象，公部門帶頭示範，逐步擴大至大型民間建築。'),
        ('② 住宅完善','BERSh 住宅版全面上線\n住宅建築能效評估系統（BERSh）評估方法完善，涵蓋集合住宅與透天，回應居住節能需求。'),
        ('③ 基準更新','EUI 基準值校正\n依最新建築耗能調查數據，重新校正各類建築的基準能源使用強度，使分級更貼近現況。'),
        ('④ 數據整合','智慧電表實測數據\n鼓勵以智慧電表（AMI）實際用電數據佐證，結合智慧建築系統，提升評估準確度。'),
        ('⑤ 淨零銜接','近零碳建築（1+ 級）路徑\n明確定義 1+ 級「近零能耗建築」標準，作為 2050 淨零建築的具體里程碑。'),
        ('⑥ 標示揭示','能效標示公開揭示\n取得標示的建築需於明顯處揭示能效等級貼標，如同家電能效標章，強化市場辨識度。'),
    ]
    for i,(badge,body) in enumerate(updates):
        col=i%3; row=i//3
        bx=Inches(1+col*4.1); by=Inches(1.85+row*2.55)
        rect(sl,bx,by,Inches(3.9),Inches(2.4),AMBER_BG)
        txb(sl,badge,bx+Inches(.12),by+Inches(.1),Inches(3.65),Inches(.35),size=13,bold=True,color=AMBER)
        title,desc=body.split('\n',1)
        txb(sl,title,bx+Inches(.12),by+Inches(.52),Inches(3.65),Inches(.35),size=13,bold=True,color=CHARCOAL)
        txb(sl,desc, bx+Inches(.12),by+Inches(.92),Inches(3.65),Inches(1.3),size=11,color=GRAY)

    # ── 05 EUI 核心概念 ────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 核心概念',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'EUI — 能源使用強度',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    rect(sl,Inches(1),Inches(1.85),Inches(6.5),Inches(3.0),AMBER_BG)
    txb(sl,'EUI 是什麼？',Inches(1.15),Inches(1.95),Inches(6.2),Inches(.35),size=13,bold=True,color=AMBER)
    txb(sl,'Energy Use Intensity（能源使用強度）\n指建築物每年每平方公尺的能源使用量：',
        Inches(1.15),Inches(2.35),Inches(6.2),Inches(.7),size=13,color=CHARCOAL)
    rect(sl,Inches(1.5),Inches(3.1),Inches(5.5),Inches(.75),WHITE)
    txb(sl,'EUI = 年總耗電量 ÷ 樓地板面積　　單位：kWh / m² · 年',
        Inches(1.6),Inches(3.18),Inches(5.3),Inches(.58),size=14,bold=True,color=AMBER,align=PP_ALIGN.CENTER)
    txb(sl,'數值越低，代表建築越節能、能效越好。',
        Inches(1.15),Inches(3.95),Inches(6.2),Inches(.4),size=13,color=CHARCOAL)
    txb(sl,'評分邏輯：與基準值比較',Inches(7.8),Inches(1.85),Inches(5),Inches(.35),size=13,bold=True,color=AMBER)
    txb(sl,'每一類建築（辦公、學校、醫院、住宅…）都有一個基準 EUI。\n將實際 EUI 與基準比較，算出節能率：',
        Inches(7.8),Inches(2.25),Inches(5),Inches(.9),size=13,color=CHARCOAL)
    rect(sl,Inches(7.8),Inches(3.2),Inches(5),Inches(.65),AMBER_BG)
    txb(sl,'節能率 = (基準EUI − 實際EUI) ÷ 基準EUI',
        Inches(7.9),Inches(3.28),Inches(4.8),Inches(.5),size=13,bold=True,color=AMBER)
    txb(sl,'舉例說明',Inches(7.8),Inches(4.0),Inches(5),Inches(.35),size=13,bold=True,color=CHARCOAL)
    txb(sl,'某辦公大樓基準 EUI 為 150，\n實際 EUI 為 90，\n節能率 = (150−90)/150 = 40%\n→ 達到約 1 級 高效能建築。',
        Inches(7.8),Inches(4.42),Inches(5),Inches(1.4),size=13,color=CHARCOAL)

    # ── 06 八個能效等級 ────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 能效等級',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'八個能效等級',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    energy_levels=[
        ('1+', G_1PLUS, WHITE,  '近零能耗建築',  '節能率 ≥ 50%，邁向淨零碳排'),
        ('1',  G_1,     WHITE,  '頂尖能效',      '節能率 40–50%'),
        ('2',  G_2,     WHITE,  '優良能效',      '節能率 30–40%（2030 新建目標）'),
        ('3',  G_3,     CHARCOAL,'良好能效',     '節能率 20–30%'),
        ('4',  G_4,     CHARCOAL,'合格能效',     '達現行法規節能基準'),
        ('5',  G_5,     WHITE,  '待改善',        '低於基準，建議節能改善'),
        ('6',  G_6,     WHITE,  '耗能偏高',      '優先輔導改善對象'),
        ('7',  G_7,     WHITE,  '高耗能',        '能效最差，亟需全面改善'),
    ]
    for i,(num,fc,tc,name,desc) in enumerate(energy_levels):
        bar_w=Inches(2.5+i*.35)
        by=Inches(1.9+i*.62)
        rect(sl,Inches(1),by,bar_w,Inches(.55),fc)
        txb(sl,num,Inches(1),by+Pt(2),bar_w,Inches(.5),size=16,bold=True,color=tc,align=PP_ALIGN.CENTER)
        txb(sl,f'{name}　{desc}',Inches(1)+bar_w+Inches(.2),by+Pt(5),Inches(9),Inches(.45),size=13,color=CHARCOAL)
    txb(sl,'節能率區間為說明示意，實際分級門檻依各類建築與建研所公告為準',
        Inches(1),Inches(6.85),Inches(11),Inches(.35),size=11,color=GRAY,italic=True)

    # ── 07 BERS vs BERSh ───────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 系統分類',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'BERS vs BERSh — 一般建築 vs 住宅',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    # header
    rect(sl,Inches(1),Inches(1.85),Inches(2.5),Inches(.42),'#44403c')
    txb(sl,'比較項目',Inches(1.05),Inches(1.9),Inches(2.4),Inches(.35),size=12,bold=True,color=WHITE)
    rect(sl,Inches(3.55),Inches(1.85),Inches(4.5),Inches(.42),AMBER)
    txb(sl,'BERS（一般建築）',Inches(3.6),Inches(1.9),Inches(4.4),Inches(.35),size=12,bold=True,color=WHITE)
    rect(sl,Inches(8.1),Inches(1.85),Inches(4.5),Inches(.42),'#92400e')
    txb(sl,'BERSh（住宅建築）',Inches(8.15),Inches(1.9),Inches(4.4),Inches(.35),size=12,bold=True,color=WHITE)
    cmp=[
        ('適用對象','辦公、商業、學校、醫院、旅館等非住宅','集合住宅、公寓大廈、透天住宅'),
        ('評估重點','空調、照明等系統能源效率為主','外殼隔熱、家電待機、自然通風採光'),
        ('使用模式','日間集中使用，空調負荷大','全天居住，耗能型態分散'),
        ('基準依據','各用途別建築實測 EUI 基準','住宅單元能耗模擬 + 實測校正'),
        ('分級方式','皆採 1+ 至 7 共八個能效等級（標示形式一致）','←同左'),
    ]
    for i,(rh,a,b) in enumerate(cmp):
        bg='#fefce8' if i%2==0 else WHITE
        y=Inches(2.35+i*.7)
        rect(sl,Inches(1),y,Inches(2.5),Inches(.65),bg)
        txb(sl,rh,Inches(1.05),y+Pt(4),Inches(2.4),Inches(.58),size=12,bold=True,color=CHARCOAL)
        if i==4:
            rect(sl,Inches(3.55),y,Inches(9.05),Inches(.65),AMBER_XP)
            txb(sl,'皆採 1+ 至 7 共八個能效等級，標示形式一致',
                Inches(3.65),y+Pt(4),Inches(8.8),Inches(.58),size=12,bold=True,color=AMBER,align=PP_ALIGN.CENTER)
        else:
            rect(sl,Inches(3.55),y,Inches(4.5),Inches(.65),bg)
            rect(sl,Inches(8.1),y,Inches(4.5),Inches(.65),bg)
            txb(sl,a,Inches(3.6),y+Pt(4),Inches(4.4),Inches(.58),size=11,color=CHARCOAL)
            txb(sl,b,Inches(8.15),y+Pt(4),Inches(4.4),Inches(.58),size=11,color=CHARCOAL)
    rect(sl,Inches(1),Inches(5.95),Inches(11.3),Inches(.95),AMBER_XP)
    txb(sl,'💡 兩套系統評估方法不同，但分級標示一致，讓民眾無論購買辦公室或住宅，\n都能用同一套「1+ 到 7」的語言理解建築能效。',
        Inches(1.15),Inches(6.0),Inches(11),Inches(.85),size=13,color=AMBER)

    # ── 08 評估系統範圍 ────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 評估範圍',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'能效評估涵蓋哪些系統？',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    systems=[
        ('❄️','空調系統','主機效率 COP/IPLV、冰水系統、變頻控制'),
        ('💡','照明系統','LED 比例、照明功率密度 LPD、自動調光'),
        ('🧱','建築外殼','外牆/屋頂隔熱、開窗比、Low-E 玻璃遮陽'),
        ('🚿','熱水系統','熱泵、太陽能熱水、鍋爐效率'),
        ('🛗','電梯動力','變頻電梯、電力回生、群控調度'),
        ('☀️','再生能源','太陽光電自發自用、儲能系統扣減'),
    ]
    for i,(icon,name,desc) in enumerate(systems):
        col=i%3; row=i//3
        bx=Inches(1+col*4.1); by=Inches(2.0+row*2.4)
        rect(sl,bx,by,Inches(3.9),Inches(2.2),AMBER_BG)
        txb(sl,icon,bx+Inches(.12),by+Inches(.1),Inches(3.65),Inches(.5),size=26)
        txb(sl,name,bx+Inches(.12),by+Inches(.7),Inches(3.65),Inches(.4),size=15,bold=True,color=AMBER)
        txb(sl,desc,bx+Inches(.12),by+Inches(1.15),Inches(3.65),Inches(.85),size=12,color=CHARCOAL)
    rect(sl,Inches(1),Inches(6.5),Inches(11.3),Inches(.75),AMBER_XP)
    txb(sl,'各系統能耗加總後換算為建築整體 EUI；其中再生能源（如屋頂太陽能）所發的電可扣減建築總耗能，\n是衝刺 1+ 近零能耗等級的關鍵。',
        Inches(1.15),Inches(6.55),Inches(11),Inches(.65),size=12,color=AMBER)

    # ── 09 三大制度關係 ────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 制度關係',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'三大制度如何分工？',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    rel=[
        ('#a7f3d0','#f0fdf4','綠建築 EEWH','全面環境品質',
         '生態、節能、減廢、健康九大面向，節能只是其中一項，範圍最廣。','#065f46'),
        ('#bfdbfe','#eff6ff','智慧建築',  '智慧化系統',
         '資訊、安全、節能管理等六大智慧系統，用科技達成管理效率。','#1e40af'),
        (AMBER_LG, AMBER_XP,'BERS 能效', '純粹能源效率',
         '聚焦單一指標 EUI，把建築能源表現量化成 1+ 到 7 的分級。',AMBER),
    ]
    for i,(bc,bg,tag,name,desc,fc) in enumerate(rel):
        bx=Inches(1+i*4.1)
        rect(sl,bx,Inches(2.0),Inches(3.9),Inches(3.3),bg)
        txb(sl,tag, bx+Inches(.15),Inches(2.1),Inches(3.6),Inches(.35),size=13,bold=True,color=fc)
        txb(sl,name,bx+Inches(.15),Inches(2.52),Inches(3.6),Inches(.4),size=16,bold=True,color=fc)
        txb(sl,desc,bx+Inches(.15),Inches(3.0),Inches(3.6),Inches(1.0),size=12,color=CHARCOAL)
    txb(sl,'三者互補而非取代：綠建築是建築的「全面健檢」，智慧建築是「智慧大腦」，而 BERS 是專注的「能效成績單」。',
        Inches(1),Inches(5.5),Inches(11.3),Inches(.55),size=14,color=CHARCOAL)
    rect(sl,Inches(1),Inches(6.1),Inches(11.3),Inches(1.0),AMBER_XP)
    txb(sl,'💡 2023 版綠建築的日常節能指標已與 BERS 銜接，智慧建築的節能管理碳足跡監控也能為 BERS 提供實測數據，\n三大制度逐步整合成完整的永續建築評估體系。',
        Inches(1.15),Inches(6.18),Inches(11),Inches(.85),size=13,color=AMBER)

    # ── 10 淨零路徑 ────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 淨零路徑',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'邁向 2050 淨零建築',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    tl=[('2024','公有新建強制申請能效標示',G_4),
        ('2027','擴大至大型民間建築',G_3),
        ('2030','新建建築達能效 2 級以上',G_2),
        ('2040','既有建築逐步改善升級',G_1),
        ('2050★','全面淨零建築 1+ 級',G_1PLUS)]
    for i,(yr,desc,fc) in enumerate(tl):
        x=Inches(1+i*2.4)
        rect(sl,x,Inches(2.0),Inches(.65),Inches(.65),fc)
        txb(sl,yr.replace('★',''),x,Inches(2.0),Inches(.65),Inches(.65),
            size=11,bold=True,color=WHITE,align=PP_ALIGN.CENTER)
        txb(sl,yr,x-Inches(.1),Inches(2.72),Inches(.95),Inches(.3),
            size=11,bold=('★' in yr),color=G_1PLUS if '★' in yr else CHARCOAL)
        txb(sl,desc,x-Inches(.2),Inches(3.05),Inches(1.05),Inches(1.0),size=10,color=GRAY)
    for i,(num,lbl,fc) in enumerate([('2 級','2030 新建目標',G_2),('1+ 級','2050 淨零目標',G_1PLUS),('≥50%','近零能耗節能率',AMBER)]):
        bx=Inches(1+i*4.1)
        rect(sl,bx,Inches(4.5),Inches(3.9),Inches(1.6),'#f9fafb')
        txb(sl,num,bx,Inches(4.6),Inches(3.9),Inches(.75),size=32,bold=True,color=fc,align=PP_ALIGN.CENTER)
        txb(sl,lbl,bx,Inches(5.35),Inches(3.9),Inches(.4),size=12,color=GRAY,align=PP_ALIGN.CENTER)

    # ── 11 申請流程 ────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl,'#fafaf9')
    txb(sl,'BERS ／ 申請流程',Inches(1),Inches(.5),Inches(5),Inches(.4),size=12,color=AMBER)
    accent_bar(sl,Inches(1),Inches(.93),Inches(1.2),AMBER)
    txb(sl,'申請流程 — 四大階段',Inches(1),Inches(1.07),Inches(11),Inches(.6),size=28,bold=True,color=CHARCOAL)
    steps=[
        ('STEP 01','📐','資料準備','蒐集建築圖說、空調照明設備規格、用電資料或能耗模擬報告'),
        ('STEP 02','🧮','EUI 計算','依評估手冊計算各系統能耗，換算建築整體 EUI 與節能率'),
        ('STEP 03','🔍','評定審查','向評定機構提送，經書面審查與必要現勘，核定能效等級'),
        ('STEP 04','🏷️','標示揭示','取得能效標示證書，於建築明顯處張貼 1+～7 級能效貼標'),
    ]
    for i,(num,icon,title,desc) in enumerate(steps):
        bx=Inches(1+i*3.1)
        rect(sl,bx,Inches(2.0),Inches(2.9),Inches(2.8),AMBER_BG)
        txb(sl,num, bx+Inches(.12),Inches(2.1),Inches(2.65),Inches(.3),size=11,color=AMBER)
        txb(sl,icon,bx+Inches(.12),Inches(2.45),Inches(2.65),Inches(.45),size=22)
        txb(sl,title,bx+Inches(.12),Inches(2.97),Inches(2.65),Inches(.4),size=14,bold=True,color=CHARCOAL)
        txb(sl,desc, bx+Inches(.12),Inches(3.42),Inches(2.65),Inches(1.15),size=11,color=GRAY)
        if i<3:
            txb(sl,'→',Inches(3.9+i*3.1),Inches(3.2),Inches(.3),Inches(.4),size=16,color=GRAY)
    rect(sl,Inches(1),Inches(5.0),Inches(5.8),Inches(2.15),AMBER_BG)
    txb(sl,'兩種評估途徑',Inches(1.15),Inches(5.1),Inches(5.5),Inches(.35),size=13,bold=True,color=AMBER)
    txb_lines(sl,['設計評估：以設計圖說與模擬數據申請（新建建築）','實測評估：以智慧電表實際用電佐證（既有建築）'],
        Inches(1.15),Inches(5.5),Inches(5.5),Inches(.9),size=12,color=CHARCOAL,bullet=True)
    rect(sl,Inches(7.1),Inches(5.0),Inches(5.8),Inches(2.15),AMBER_XP)
    txb(sl,'標示有效期',Inches(7.25),Inches(5.1),Inches(5.5),Inches(.35),size=13,bold=True,color=AMBER)
    txb(sl,'能效標示證書有效期一般為 3～5 年，\n建築完成節能改善後可重新評估升級，\n鼓勵持續精進能源表現。',
        Inches(7.25),Inches(5.5),Inches(5.5),Inches(1.4),size=12,color=CHARCOAL)

    # ── 12 結語 ────────────────────────────────
    sl = blank_slide(prs)
    fill_bg(sl, STONE)
    txb(sl,'建築能效評估標示 BERS 2024 版',
        Inches(1),Inches(.8),Inches(10),Inches(.4),size=13,color=AMBER_LG)
    txb(sl,'把建築的能源表現，',
        Inches(1),Inches(1.4),Inches(11),Inches(.7),size=36,bold=True,color=WHITE)
    txb(sl,'變成看得懂的一張成績單',
        Inches(1),Inches(2.1),Inches(11),Inches(.7),size=36,bold=True,color=AMBER_LG)
    rect(sl,Inches(1),Inches(2.95),Inches(.7),Pt(4),AMBER_LG)
    txb(sl,'從 EUI 量化到 1+ 至 7 的能效分級，BERS 讓建築節能不再是模糊概念。\n配合 2050 淨零路徑，每一棟達到高能效等級的建築，\n都是邁向永續未來的一塊堅實基石。',
        Inches(1),Inches(3.15),Inches(10),Inches(1.5),size=16,color='#a8a29e')
    # mini energy scale
    for i,(num,fc) in enumerate([('1+',G_1PLUS),('1',G_1),('2',G_2),('3',G_3),
                                   ('4',G_4),('5',G_5),('6',G_6),('7',G_7)]):
        bx=Inches(1+i*.65)
        h=Inches(.55-i*.04) if i<6 else Inches(.25)
        rect(sl,bx,Inches(5.5),Inches(.55),h,fc)
        if i==0:
            txb(sl,num,bx,Inches(5.5),Inches(.55),h,size=9,bold=True,color=WHITE,align=PP_ALIGN.CENTER)
    txb(sl,'資料來源：內政部建築研究所 建築能效評估手冊 2024 版',
        Inches(1),Inches(6.8),Inches(11),Inches(.35),size=11,color='#44403c',italic=True)

    prs.save(path)
    print(f'Saved {path}')

build_bers('/home/user/jieceng-web/presentation-BERS.pptx')
print('BERS done')
