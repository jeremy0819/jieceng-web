"""Build the EEWH green-building deck (presentation-EEWH.pptx).

Mirrors public/presentation.html: four-category structure (生態・節能・減廢・
健康) for sales agents and clients. Emoji-free, professional layout.
"""
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import deck_lib as D

DARK = "#1a1a1a"
EM = "#064e3b"; EM_LG = "#10b981"
ECO = "#047857"; ENERGY = "#0369a1"; WASTE = "#b45309"; HEALTH = "#b91c1c"
WARM = D.WARM; CHAR = D.CHAR; BODY = D.BODY; STONE4 = D.STONE4; LINE = D.LINE; WHITE = D.WHITE


def content(prs):
    sl = D.blank(prs); D.fill_bg(sl, WARM)
    return sl


def indicator(prs, cat, accent, pts, en, name, subhead, items, feel, mandatory=False):
    sl = content(prs)
    D.text(sl, cat, Inches(0.9), Inches(0.7), Inches(9), Inches(0.3),
           size=10, color=STONE4, font=D.MONO)
    lx, ly = Inches(0.9), Inches(1.75)
    if mandatory:
        D.rect(sl, lx, ly, Inches(1.85), Inches(0.34), fill=accent)
        D.text(sl, "門檻指標・必過", lx, ly + Pt(4), Inches(1.85), Inches(0.28),
               size=9, color=WHITE, font=D.MONO, align=PP_ALIGN.CENTER)
        ly = ly + Inches(0.52)
    D.rect(sl, lx, ly, Inches(2.45), Inches(1.5), fill=WHITE, line=LINE)
    D.rect(sl, lx, ly, Pt(2.6), Inches(1.5), fill=accent)
    D.text(sl, pts, lx + Inches(0.22), ly + Inches(0.16), Inches(2.1), Inches(0.7),
           size=34, bold=True, color=accent)
    D.text(sl, en, lx + Inches(0.22), ly + Inches(1.02), Inches(2.15), Inches(0.3),
           size=8.5, color=STONE4, font=D.MONO)
    D.text(sl, name, lx, ly + Inches(1.7), Inches(2.7), Inches(0.5),
           size=18, bold=True, color=accent)
    rx, ry = Inches(4.0), Inches(1.75)
    D.text(sl, subhead, rx, ry, Inches(8.3), Inches(0.4), size=14, bold=True, color=CHAR)
    D.bullets(sl, items, rx, ry + Inches(0.55), Inches(8.3), Inches(2.3),
              size=12.5, color=BODY, marker_color=accent, gap=5, spacing=1.18)
    fy = ry + Inches(0.55) + Inches(0.44) * len(items) + Inches(0.25)
    if fy > Inches(5.5):
        fy = Inches(5.5)
    D.rect(sl, rx, fy, Pt(2), Inches(0.95), fill=accent)
    D.text(sl, feel, rx + Inches(0.2), fy, Inches(7.9), Inches(1.0),
           size=12, italic=True, color=accent, spacing=1.2)


def build(path):
    prs = D.new_prs()

    # 01 cover
    D.cover(prs, DARK, "EEWH ｜ 綠建築標章", "綠建築，\n到底好在哪裡？", EM_LG,
            "從生態、節能、減廢到健康，四個面向看懂一棟好房子，\n該為住戶把關些什麼。")

    # 02 四大範疇總覽
    sl = content(prs)
    D.header(sl, "EEWH ｜ ECOLOGY · ENERGY · WASTE · HEALTH", "綠建築的四大範疇", EM)
    D.lead(sl, "綠建築標章的英文縮寫 EEWH，正是四個面向的字首：生態（Ecology）、節能"
               "（Energy saving）、減廢（Waste reduction）、健康（Health）。一棟房子在這四"
               "件事上做得好，才稱得上綠建築。", y=Inches(1.95))
    D.card_row(sl, [
        dict(accent=ECO, idx="ECOLOGY", head="生態", head_color=ECO, body="基地與自然共生"),
        dict(accent=ENERGY, idx="ENERGY", head="節能", head_color=ENERGY, body="日常用電用得更少"),
        dict(accent=WASTE, idx="WASTE", head="減廢", head_color=WASTE, body="建造過程低碳低污染"),
        dict(accent=HEALTH, idx="HEALTH", head="健康", head_color=HEALTH, body="室內環境宜居宜人"),
    ], y=Inches(3.5), h=Inches(2.0))

    # 03 什麼是綠建築
    sl = content(prs)
    D.header(sl, "定義", "什麼是綠建築", EM)
    D.lead(sl, "依內政部定義，綠建築是在建築的整個生命週期裡 —— 從生產、規劃、施工、使用、"
               "維護到拆除 —— 消耗最少地球資源、製造最少廢棄物的建築物。", y=Inches(1.95))
    D.rect(sl, Inches(0.9), Inches(3.4), Inches(11.53), Inches(1.7), fill=EM)
    D.text(sl, "換句話說，綠建築是一種對環境友善、同時讓住戶住得更省、更舒適、更安心的房子。"
               "它不是附加的裝飾，而是貫穿設計與施工的整套思維。",
           Inches(1.25), Inches(3.75), Inches(10.8), Inches(1.1),
           size=15, color=WHITE, spacing=1.4)

    # 04 公信力
    sl = content(prs)
    D.header(sl, "制度背景", "由內政部把關的官方標章", EM)
    D.card_row(sl, [
        dict(accent=EM, head=None, body=None),
        dict(accent=EM, head=None, body=None),
        dict(accent=EM, head=None, body=None),
    ], y=Inches(2.1), h=Inches(3.0))
    facts = [("1999", "創立年份", "台灣自 1999 年推動，是全球第四套、亞洲第一套綠建築評估系統。"),
             ("9", "項評估指標", "分屬生態、節能、減廢、健康四大範疇，滿分 100 分。"),
             ("5", "個認證等級", "由合格至鑽石分五級，須經第三方專業審查，不是建商自說自話。")]
    cw = (Inches(11.53) - Inches(0.28) * 2) / 3
    for i, (num, cap, desc) in enumerate(facts):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.text(sl, num, x + Inches(0.25), Inches(2.45), cw - Inches(0.4), Inches(0.8),
               size=34, bold=True, color=EM)
        D.text(sl, cap, x + Inches(0.25), Inches(3.25), cw - Inches(0.4), Inches(0.3),
               size=11, color=STONE4)
        D.rect(sl, x + Inches(0.25), Inches(3.7), cw - Inches(0.5), Pt(1), fill=LINE)
        D.text(sl, desc, x + Inches(0.25), Inches(3.9), cw - Inches(0.5), Inches(1.1),
               size=11, color=BODY, spacing=1.25)
    D.note(sl, "2023 年版更與建築能效評估（BERS）接軌，是台灣邁向淨零建築的核心制度之一。")

    # 05 配分架構
    sl = content(prs)
    D.header(sl, "評估架構", "四大範疇　九大指標　滿分 100", EM)
    scope = [("27", "生態", ECO, "生物多樣性\n綠化量\n基地保水"),
             ("32", "節能（配分最高）", ENERGY, "日常節能\n外殼・空調・照明"),
             ("16", "減廢", WASTE, "CO₂ 減量\n廢棄物減量"),
             ("25", "健康", HEALTH, "室內環境\n水資源\n污水垃圾")]
    cw = (Inches(11.53) - Inches(0.28) * 3) / 4
    for i, (num, cap, ac, body) in enumerate(scope):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.1), cw, Inches(3.0), fill=WHITE, line=LINE)
        D.rect(sl, x, Inches(2.1), cw, Pt(2.6), fill=ac)
        D.text(sl, num, x + Inches(0.22), Inches(2.3), cw - Inches(0.4), Inches(0.7),
               size=30, bold=True, color=ac)
        D.text(sl, cap, x + Inches(0.22), Inches(3.05), cw - Inches(0.4), Inches(0.5),
               size=10.5, color=STONE4)
        D.rect(sl, x + Inches(0.22), Inches(3.55), cw - Inches(0.44), Pt(1), fill=LINE)
        D.text(sl, body, x + Inches(0.22), Inches(3.72), cw - Inches(0.4), Inches(1.3),
               size=11, color=BODY, spacing=1.3)
    D.note(sl, "節能配分最高（32 分），制度刻意把住戶最有感的「省」放在第一位。")

    # 06 divider 生態
    D.divider(prs, EM, "ECOLOGY ｜ 生態範疇・27 分", "生態",
              "把綠意與生命力留在基地裡，讓社區本身就像一座會呼吸的公園。",
              "#d1fae5", EM_LG)
    # 07-09
    indicator(prs, "生態範疇　01 / 03", ECO, "9 分", "BIODIVERSITY", "生物多樣性",
              "在社區裡看得見的設計",
              ["連貫的綠帶與中庭花園，串起綠地", "生態池、小型水域與綠塊，提供小生物棲地",
               "優先選用原生與誘鳥誘蝶植物", "友善土壤、減少夜間人工照明的光害"],
              "住進來之後，早晨會有鳥鳴、四季有花開 —— 綠意是日常的一部分，不是樣品屋裡的擺設。")
    indicator(prs, "生態範疇　02 / 03", ECO, "9 分", "GREENERY", "綠化量",
              "不只是種樹，是種對樹",
              ["喬木、灌木、花圃構成多層次綠化", "大小喬木混植，形成接近自然的生態複層",
               "屋頂花園與人工地盤綠化，向上延伸綠量", "以植栽四十年的固碳量作為評估基準"],
              "樹蔭能降溫、綠視野能放鬆 —— 夏天體感更涼，景觀也更耐看、更保值。")
    indicator(prs, "生態範疇　03 / 03", ECO, "9 分", "SOIL WATER CONTENT", "基地保水",
              "讓土地留得住水",
              ["透水鋪面與透水性綠地，雨水滲得進去", "雨水花園、滲透井等貯留滲透設計",
               "降低不透水硬鋪面的比例", "替城市分擔排洪、緩解都市熱島"],
              "大雨天社區不易積水，微氣候也更涼爽，住起來更安心。")

    # 10 divider 節能
    D.divider(prs, EM, "ENERGY SAVING ｜ 節能範疇・32 分", "節能",
              "配分最高的一塊。節能省下的每一度電、每一塊錢，最後都回到住戶口袋。",
              "#d1fae5", EM_LG)
    indicator(prs, "節能範疇　配分 32 分", ENERGY, "32 分", "DAILY ENERGY SAVING", "日常節能",
              "評的是天天都在用的三件事",
              ["建築外殼：隔熱、遮陽、開窗設計，把室外的熱擋在外面",
               "空調系統：高效率主機與變頻控制，同樣的涼用更少電",
               "照明系統：LED 高效率燈具與照明規劃"],
              "這是兩項門檻指標之一 —— 沒通過就拿不到標章。買綠建築，省電是被制度保證的。",
              mandatory=True)
    # 12 節能設計手法
    sl = content(prs)
    D.header(sl, "節能 · 設計手法", "涼快，是設計出來的", ENERGY)
    D.card_row(sl, [
        dict(accent=ENERGY, head="外殼隔熱", head_color=ENERGY, body="屋頂與外牆的隔熱層，把熱阻擋在室外"),
        dict(accent=ENERGY, head="開窗遮陽", head_color=ENERGY, body="遮陽板與 Low-E 玻璃，採光不必承受西曬"),
        dict(accent=ENERGY, head="高效空調", head_color=ENERGY, body="變頻與高效率主機，降低長期空調耗電"),
        dict(accent=ENERGY, head="LED 照明", head_color=ENERGY, body="高效率燈具與感應控制，公共電費更省"),
    ], y=Inches(2.2), h=Inches(2.0))
    D.rect(sl, Inches(0.9), Inches(4.7), Pt(2), Inches(0.6), fill=ENERGY)
    D.text(sl, "每個月的電費單，就是綠建築最誠實的成績單。",
           Inches(1.1), Inches(4.75), Inches(10), Inches(0.6), size=13,
           italic=True, color=ENERGY)

    # 13 divider 減廢
    D.divider(prs, EM, "WASTE REDUCTION ｜ 減廢範疇・16 分", "減廢",
              "綠建築的功夫不只在交屋後。從動工的第一天，建造過程本身就要對環境負責。",
              "#d1fae5", EM_LG)
    indicator(prs, "減廢範疇　01 / 02", WASTE, "8 分", "CO₂ REDUCTION", "CO₂ 減量",
              "蓋房子，也要把碳算進去",
              ["結構合理化、輕量化，少用不必要的材料", "採用再生與低碳建材",
               "優先使用在地建材，減少運輸碳排", "評估建材生產階段的 CO₂ 排放"],
              "在 ESG 與淨零成為共識的時代，低碳建造讓這個家從出生就是一項低碳資產。")
    indicator(prs, "減廢範疇　02 / 02", WASTE, "8 分", "WASTE REDUCTION", "廢棄物減量",
              "乾淨的工地，通常帶來可靠的品質",
              ["土方平衡，減少棄土外運", "營建自動化與乾式施工",
               "施工揚塵與噪音的防制管理", "舊建築再利用，保留還能用的結構"],
              "施工管理嚴謹的建案，交屋時的細節品質往往也更讓人放心。")

    # 16 divider 健康
    D.divider(prs, EM, "HEALTH ｜ 健康範疇・25 分", "健康",
              "隔音、採光、通風、好空氣、好水質 —— 這些看不見的設計，才是每天住得舒不舒服的關鍵。",
              "#d1fae5", EM_LG)
    indicator(prs, "健康範疇　01 / 03", HEALTH, "12 分", "INDOOR ENVIRONMENT", "室內環境",
              "健康範疇裡配分最高的一項",
              ["安靜：隔音與樓板衝擊音控制，樓上腳步聲不擾眠", "明亮：自然採光與照明品質",
               "通風：自然通風設計，維持良好空氣品質", "低污染：低逸散健康綠建材，減少甲醛等逸散"],
              "對家中的長輩與孩子來說，一個安靜、明亮、好空氣的家，是最實在的承諾。")
    indicator(prs, "健康範疇　02 / 03", HEALTH, "8 分", "WATER RESOURCE", "水資源",
              "省水，同樣被制度保證",
              ["省水標章馬桶與節水龍頭", "雨水回收再利用系統",
               "中水（生活雜排水）回收", "節水澆灌與用水計量管理"],
              "水資源與日常節能並列兩大門檻，沒通過就沒有標章。水費單，也會替綠建築說話。",
              mandatory=True)
    indicator(prs, "健康範疇　03 / 03", HEALTH, "5 分", "SEWAGE & GARBAGE", "污水垃圾改善",
              "社區的體面，藏在這些細節裡",
              ["完善的污水接管與處理", "專用的垃圾分類與暫存空間",
               "順暢的資源回收動線與設施", "景觀化、衛生化的垃圾處理區"],
              "垃圾間不髒不臭、回收動線順，是入住之後天天有感的生活品質。")

    # 20 兩項門檻
    sl = content(prs)
    D.header(sl, "關鍵機制", "兩項門檻，雙重保證", EM)
    D.lead(sl, "九大指標裡，有兩項是「門檻指標」—— 不是有做就好，而是必須做到。只要任一項"
               "未通過，無論總分多高，都拿不到綠建築標章。", y=Inches(1.95))
    D.card_row(sl, [
        dict(accent=ENERGY, head="日常節能", head_color=ENERGY,
             body="外殼、空調、照明的節能表現必須達到基準，回應的是缺電時代的壓力。"),
        dict(accent=HEALTH, head="水資源", head_color=HEALTH,
             body="節水器材與雨中水回收必須達到節水基準，回應的是缺水時代的挑戰。"),
    ], y=Inches(3.45), h=Inches(1.7))
    D.note(sl, "其餘七項指標雖非門檻，但會給予基本分；申請時通常會盡量爭取，以拉高總分與等級。")

    # 21 五大等級
    sl = content(prs)
    D.header(sl, "認證等級", "從合格到鑽石，分五個等級", EM)
    D.lead(sl, "依總得分在歷年案件中的相對表現分級，特性是「合格容易、高分難」，等級愈高愈稀有。",
           y=Inches(1.95))
    levels = [("合格級", "基本門檻", EM), ("銅級", "中上表現", "#92400e"),
              ("銀級", "良好", "#475569"), ("黃金級", "優異", "#b45309"),
              ("鑽石級", "最高等級", "#6d28d9")]
    cw = (Inches(11.53) - Inches(0.22) * 4) / 5
    for i, (nm, cap, ac) in enumerate(levels):
        x = Inches(0.9) + (cw + Inches(0.22)) * i
        D.rect(sl, x, Inches(3.0), cw, Inches(1.7), fill=WHITE, line=LINE)
        D.rect(sl, x, Inches(3.0), cw, Pt(2.6), fill=ac)
        D.text(sl, nm, x, Inches(3.45), cw, Inches(0.4), size=15, bold=True,
               color=ac, align=PP_ALIGN.CENTER)
        D.text(sl, cap, x, Inches(3.95), cw, Inches(0.3), size=10, color=STONE4,
               align=PP_ALIGN.CENTER)
    D.note(sl, "等級依得分機率分布劃分（鑽石級約落在歷年案件前段班）。介紹個案時，以該案實際"
               "取得的等級與證書為準。")

    # 22 申請流程
    sl = content(prs)
    D.header(sl, "取得方式", "一張標章，經過四道把關", EM)
    steps = [("01", "設計導入", "規劃階段就把九大指標放進設計裡"),
             ("02", "候選證書", "動工前以設計圖說通過審查，取得候選綠建築證書"),
             ("03", "施工查核", "按圖施作、保留查驗文件與照片"),
             ("04", "正式標章", "完工查核後核發，標章有效期屆滿需複評展延")]
    cw = (Inches(11.53) - Inches(0.28) * 3) / 4
    for i, (n, h, b) in enumerate(steps):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.5), cw, Inches(2.2), fill=WHITE, line=LINE)
        D.text(sl, n, x + Inches(0.22), Inches(2.72), cw - Inches(0.4), Inches(0.3),
               size=11, color=EM, font=D.MONO)
        D.text(sl, h, x + Inches(0.22), Inches(3.12), cw - Inches(0.4), Inches(0.4),
               size=14, bold=True, color=CHAR)
        D.text(sl, b, x + Inches(0.22), Inches(3.62), cw - Inches(0.4), Inches(1.0),
               size=11, color=BODY, spacing=1.25)
    D.note(sl, "預售階段多半持有的是「候選綠建築證書」，完工通過查核後才換發正式標章 —— 這正是"
               "制度可信的原因。")

    # 23 選綠建築理由
    sl = content(prs)
    D.header(sl, "給購屋者", "為什麼值得選綠建築", EM)
    D.card_row(sl, [
        dict(accent=ENERGY, head="省得有感", head_color=ENERGY, body="節能與節水是必過門檻，長期水電費實際降低"),
        dict(accent=HEALTH, head="住得健康", head_color=HEALTH, body="隔音、採光、通風與綠建材，全家天天受益"),
        dict(accent=EM, head="品質有據", head_color=EM, body="內政部認證、第三方審查，看證書不必聽話術"),
        dict(accent=WASTE, head="資產保值", head_color=WASTE, body="對接淨零趨勢的低碳資產，市場辨識度高"),
    ], y=Inches(2.3), h=Inches(2.1))

    # 24 傑丞實績
    sl = content(prs)
    D.header(sl, "實績", "傑丞建築機構的綠建築實績", EM)
    D.card_row(sl, [
        dict(accent=EM, idx="RESIDENTIAL · 2024", head="台北市 信義區", head_color=EM, body="住宅型 EEWH-RS"),
        dict(accent=EM, idx="COMMERCIAL · 2023", head="新北市 板橋區", head_color=EM, body="商辦複合"),
        dict(accent=EM, idx="LANDSCAPE · 2024", head="台中市 西屯區", head_color=EM, body="景觀生態社區"),
        dict(accent=EM, idx="RENOVATION · 2023", head="台北市 大同區", head_color=EM, body="舊建築改善"),
    ], y=Inches(2.3), h=Inches(2.1))
    D.note(sl, "以上為代表案例類型，實際標章等級依各案核定文件為準。")

    # 25 重點回顧
    sl = content(prs)
    D.header(sl, "重點回顧", "四句話記住綠建築", EM)
    D.bullets(sl, [
        "生態（27 分）：綠意、生態與會呼吸的土地，社區像一座公園",
        "節能（32 分）：配分最高且為必過門檻，省下的都回到住戶身上",
        "減廢（16 分）：低碳建造，從出生就是低碳資產",
        "健康（25 分）：安靜、明亮、通風、好空氣，省水同樣是必過門檻",
    ], Inches(0.9), Inches(2.2), Inches(11.3), Inches(3), size=15, color=BODY,
        marker_color=EM_LG, gap=10, spacing=1.2)
    D.note(sl, "內政部官方認證，五級分明（合格至鑽石），1999 年推行至今、亞洲第一套。"
               "介紹個案時，請以該案實際證書等級與內政部最新規定為準。")

    # 26 closing
    D.closing(prs, DARK, "EEWH ｜ 生態・節能・減廢・健康",
              "更省、更健康、更值得\n傳承的居住選擇", EM_LG)

    prs.save(path)
    print(f"saved {path} · {len(prs.slides._sldIdLst)} slides")


if __name__ == "__main__":
    build("/home/user/jieceng-web/presentation-EEWH.pptx")
