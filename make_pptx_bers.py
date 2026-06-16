"""Build the BERS building-energy deck (presentation-BERS.pptx).

Mirrors public/presentation-bers.html: energy-efficiency rating, near-zero-carbon
building and the net-zero pathway. Emoji-free; uses an EU-style 7-tier energy
gradient scale.
"""
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import deck_lib as D

DARK = "#1c1917"
AMBER = "#b45309"; AMBER_MID = "#d97706"; AMBER_LG = "#fbbf24"; AMBER_PALE = "#fef3c7"
TIERS = ["#047857", "#059669", "#34d399", "#a3e635", "#facc15", "#fb923c", "#f87171", "#dc2626"]
WARM = D.WARM; CHAR = D.CHAR; BODY = D.BODY; STONE4 = D.STONE4; LINE = D.LINE; WHITE = D.WHITE


def content(prs):
    sl = D.blank(prs); D.fill_bg(sl, WARM)
    return sl


def eui_item(prs, idx, en, name, subhead, items, feel):
    sl = content(prs)
    D.text(sl, f"EUI 檢核項目　{idx:02d} / 06", Inches(0.9), Inches(0.7), Inches(9), Inches(0.3),
           size=10, color=STONE4, font=D.MONO)
    lx, ly = Inches(0.9), Inches(1.75)
    D.rect(sl, lx, ly, Inches(2.45), Inches(1.5), fill=WHITE, line=LINE)
    D.rect(sl, lx, ly, Pt(2.6), Inches(1.5), fill=AMBER)
    D.text(sl, f"{idx:02d}", lx + Inches(0.22), ly + Inches(0.16), Inches(2.1), Inches(0.7),
           size=34, bold=True, color=AMBER)
    D.text(sl, en, lx + Inches(0.22), ly + Inches(1.02), Inches(2.15), Inches(0.3),
           size=8.5, color=STONE4, font=D.MONO)
    D.text(sl, name, lx, ly + Inches(1.7), Inches(2.7), Inches(0.5),
           size=18, bold=True, color=AMBER)
    rx, ry = Inches(4.0), Inches(1.75)
    D.text(sl, subhead, rx, ry, Inches(8.3), Inches(0.4), size=14, bold=True, color=CHAR)
    D.bullets(sl, items, rx, ry + Inches(0.55), Inches(8.3), Inches(2.3),
              size=12.5, color=BODY, marker_color=AMBER, gap=5, spacing=1.18)
    fy = ry + Inches(0.55) + Inches(0.44) * len(items) + Inches(0.25)
    if fy > Inches(5.5):
        fy = Inches(5.5)
    D.rect(sl, rx, fy, Pt(2), Inches(0.95), fill=AMBER)
    D.text(sl, feel, rx + Inches(0.2), fy, Inches(7.9), Inches(1.0),
           size=12, italic=True, color=AMBER, spacing=1.2)


def build(path):
    prs = D.new_prs()

    # 01 cover
    D.cover(prs, DARK, "BERS ｜ 建築能效評估標示", "把建築的能效\n標示出來", AMBER_LG,
            "能效分級、近零碳建築，以及邁向 2050 淨零的這條路，\n對開發案到底意味著什麼。")

    # 02 議程
    sl = content(prs)
    D.header(sl, "AGENDA", "本場簡報的四個部分", AMBER_MID)
    D.card_row(sl, [
        dict(accent=AMBER_MID, idx="PART 01", head="為什麼需要建築能效", head_color=CHAR,
             body="淨零趨勢、台灣淨零路徑、制度沿革、師法歐盟 EPBD"),
        dict(accent=AMBER_MID, idx="PART 02", head="能效分級制度", head_color=CHAR,
             body="相對分級的核心概念、七階段分級、近零碳建築、能效標示"),
    ], y=Inches(2.1), h=Inches(2.1))
    D.card_row(sl, [
        dict(accent=AMBER_MID, idx="PART 03", head="評估系統與範圍", head_color=CHAR,
             body="能效計算邊界、設計策略、新建與既有、適用類組、與綠建築的關係"),
        dict(accent=AMBER_MID, idx="PART 04", head="對開發案與淨零", head_color=CHAR,
             body="政策強制要求、產品價值、三標章整合、申請流程"),
    ], y=Inches(4.45), h=Inches(2.1))

    # 03 divider
    D.divider(prs, DARK, "PART 01", "為什麼需要建築能效",
              "從淨零目標，看 BERS 為什麼誕生。", AMBER_PALE, AMBER_LG)

    # 04 什麼是 BERS
    sl = content(prs)
    D.header(sl, "定義", "什麼是建築能效評估（BERS）", AMBER_MID)
    D.lead(sl, "BERS 把一棟建築的能源效率量化、分級，再「標示」出來。就像家電的能效標章一樣，"
               "讓建築的耗能表現一眼就看得懂，是推動淨零建築最有效的政策工具之一。", y=Inches(1.95))
    D.card_row(sl, [
        dict(accent=AMBER_MID, head="量化", head_color=AMBER, body="以耗能與碳排密度計算能效"),
        dict(accent=AMBER_MID, head="分級", head_color=AMBER, body="對照市場基準，分為七個階段"),
        dict(accent=AMBER_MID, head="標示", head_color=AMBER, body="公開揭露，能被檢視也能被比較"),
    ], y=Inches(3.5), h=Inches(1.8))

    # 05 全球淨零趨勢
    sl = content(prs)
    D.header(sl, "背景", "全球淨零的脈絡", AMBER_MID)
    D.card_row(sl, [
        dict(accent=AMBER_MID, idx="1997", body="《京都議定書》提出溫室氣體減量"),
        dict(accent=AMBER_MID, idx="2015", body="《巴黎協定》提出淨零排放目標"),
        dict(accent=AMBER_MID, idx="2021", body="國際能源署發表 2050 淨零路徑報告"),
        dict(accent=AMBER_MID, idx="2022", body="國發會發布台灣 2050 淨零排放路徑"),
    ], y=Inches(2.5), h=Inches(1.9))

    # 06 台灣三里程碑
    sl = content(prs)
    D.header(sl, "台灣淨零建築路徑", "三個法定的時間點", AMBER_MID)
    miles = [("2030", AMBER, "所有公有新建建築，須達建築能效 1 級或近零碳建築。"),
             ("2040", AMBER_MID, "50% 既有建築更新為能效 1 級或近零碳建築。"),
             ("2050", "#92400e", "100% 新建、逾 85% 建築為近零碳建築。")]
    cw = (Inches(11.53) - Inches(0.28) * 2) / 3
    for i, (yr, ac, desc) in enumerate(miles):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.3), cw, Inches(2.4), fill=WHITE, line=LINE)
        D.rect(sl, x, Inches(2.3), cw, Pt(2.6), fill=ac)
        D.text(sl, yr, x + Inches(0.25), Inches(2.55), cw - Inches(0.4), Inches(0.7),
               size=32, bold=True, color=ac)
        D.rect(sl, x + Inches(0.25), Inches(3.35), cw - Inches(0.5), Pt(1), fill=LINE)
        D.text(sl, desc, x + Inches(0.25), Inches(3.55), cw - Inches(0.5), Inches(1.0),
               size=12, color=BODY, spacing=1.3)
    D.note(sl, "這是淨零建築政策的法定時程，而 BERS 正是落實與檢核的關鍵工具。")

    # 07 制度沿革
    sl = content(prs)
    D.header(sl, "制度沿革", "從節能法規到能效標示", AMBER_MID)
    road = [("1995", "制訂建築節約能源設計法規"),
            ("1999", "啟動綠建築標章制度"),
            ("2022", "開始實施建築能效評估及標示，公布 EEWH-BERS 前導版（6 類 12 組）"),
            ("2023", "修正綠建築標章及建築能效標示的申請審核作業要點"),
            ("2024", "發布 BERS 手冊，適用範圍擴及大部分建築類組")]
    y = Inches(2.2)
    for yr, desc in road:
        D.text(sl, yr, Inches(0.9), y, Inches(1.1), Inches(0.4), size=15, bold=True,
               color=AMBER, font=D.MONO)
        D.text(sl, desc, Inches(2.2), y, Inches(10.2), Inches(0.5), size=13, color=BODY)
        D.rect(sl, Inches(0.9), y + Inches(0.55), Inches(11.53), Pt(0.75), fill=LINE)
        y += Inches(0.78)

    # 08 EPBD
    sl = content(prs)
    D.header(sl, "制度源頭", "師法歐盟的 EPBD 能效標示", AMBER_MID)
    D.lead(sl, "BERS 仿自歐盟建築能效法令 EPBD，採用 EN 15217 建議的七階段分級標示，是國際公認"
               "最有效的淨零建築政策之一。", y=Inches(1.95))
    D.card_row(sl, [
        dict(accent=AMBER_MID, head="公開揭露", head_color=AMBER, body="能效資訊透明，能被檢視"),
        dict(accent=AMBER_MID, head="有感標示", head_color=AMBER, body="像家電能效標章，民眾看得懂"),
        dict(accent=AMBER_MID, head="市場基準", head_color=AMBER, body="以現行市場平均能效為比較基準"),
        dict(accent=AMBER_MID, head="1+ 額外級", head_color=AMBER, body="允許標示更高的近零碳等級"),
    ], y=Inches(3.4), h=Inches(1.9))

    # 09 關鍵戰場
    sl = content(prs)
    D.header(sl, "為什麼是建築", "建築，是淨零的關鍵戰場", AMBER_MID)
    D.lead(sl, "建築物的營建與長期使用，佔全國能源消耗與碳排放相當高的比重。提升建築能效，是最"
               "直接、也最有效的減碳途徑之一。", y=Inches(1.95))
    D.card_row(sl, [
        dict(accent=AMBER_MID, head="營運能耗", head_color=AMBER, body="空調、照明、設備的長期用電"),
        dict(accent=AMBER_MID, head="隱含碳", head_color=AMBER, body="建材生產與營建過程的碳排"),
        dict(accent=AMBER_MID, head="長生命週期", head_color=AMBER, body="建築一用數十年，影響深遠"),
        dict(accent=AMBER_MID, head="可管理", head_color=AMBER, body="能效可量化、可改善、可檢核"),
    ], y=Inches(3.4), h=Inches(1.9))

    # 10 divider
    D.divider(prs, DARK, "PART 02", "能效分級制度",
              "從 1+ 到 7，把建築能效講清楚。", AMBER_PALE, AMBER_LG)

    # 11 相對分級
    sl = content(prs)
    D.header(sl, "核心概念", "BERS 是一種「相對分級」", AMBER_MID)
    D.lead(sl, "BERS 以現行建築市場的平均能效水準作為合格分界，再依設計能效相對基準的優劣，往上"
               "或往下分級。", y=Inches(1.95))
    D.card_row(sl, [
        dict(accent=TIERS[1], head="優於基準", head_color="#047857",
             body_items=["切割為 5 個等分間距", "由佳至差為 1+、1、2、3、4", "達 90 分以上即進入 1+ 近零碳區間"]),
        dict(accent=TIERS[7], head="劣於基準", head_color="#dc2626",
             body_items=["不及格區間為 5、6、7", "6、7 屬能效極差的建築", "給予兩倍較寬的間距"]),
    ], y=Inches(3.3), h=Inches(2.0))

    # 12 七階段分級 scale
    sl = content(prs)
    D.header(sl, "七階段分級", "1+ 到 7，一眼看懂能效", AMBER_MID)
    labels = [("1+", "近零碳"), ("1", "能效最佳"), ("2", "優於基準"), ("3", "良好"),
              ("4", "合格分界"), ("5", "略低基準"), ("6", "能效差"), ("7", "能效極差")]
    gap = Inches(0.08)
    cw = (Inches(11.53) - gap * 7) / 8
    for i, (tier, cap) in enumerate(labels):
        x = Inches(0.9) + (cw + gap) * i
        D.rect(sl, x, Inches(2.7), cw, Inches(1.0), fill=TIERS[i])
        tc = "#1c1917" if i in (2, 3, 4) else WHITE
        D.text(sl, tier, x, Inches(2.98), cw, Inches(0.5), size=18, bold=True,
               color=tc, align=PP_ALIGN.CENTER, font=D.MONO)
        D.text(sl, cap, x, Inches(3.85), cw, Inches(0.3), size=8.5, color=STONE4,
               align=PP_ALIGN.CENTER)
    D.text(sl, "能效佳", Inches(0.9), Inches(4.35), Inches(3), Inches(0.3), size=10,
           color=STONE4, font=D.MONO)
    D.text(sl, "能效差", Inches(9.43), Inches(4.35), Inches(3), Inches(0.3), size=10,
           color=STONE4, font=D.MONO, align=PP_ALIGN.RIGHT)
    D.note(sl, "「1+」為近零碳建築（NZCB）；「4」與「5」之間，是市場平均能效的合格分界點。")

    # 13 近零碳 1+
    sl = content(prs)
    D.header(sl, "最高等級", "1+　近零碳建築（NZCB）", AMBER_MID)
    pairs = [("住宅建築", "30%", "減碳率達 30% 以上", TIERS[0]),
             ("非住宅建築", "50%", "節能率達 50% 以上", AMBER)]
    cw = (Inches(11.53) - Inches(0.28)) / 2
    for i, (h, big, b, ac) in enumerate(pairs):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.2), cw, Inches(2.0), fill=WHITE, line=LINE)
        D.rect(sl, x, Inches(2.2), cw, Pt(2.6), fill=ac)
        D.text(sl, h, x + Inches(0.25), Inches(2.45), cw - Inches(0.4), Inches(0.4),
               size=14, bold=True, color=CHAR)
        D.text(sl, big, x + Inches(0.25), Inches(2.9), cw - Inches(0.4), Inches(0.8),
               size=38, bold=True, color=ac)
        D.text(sl, b, x + Inches(0.25), Inches(3.75), cw - Inches(0.4), Inches(0.3),
               size=12, color=BODY)
    D.rect(sl, Inches(0.9), Inches(4.6), Pt(2), Inches(0.6), fill=AMBER_LG)
    D.text(sl, "對應能效分級 90 分以上的區間，是 2050 淨零建築政策的核心目標。",
           Inches(1.1), Inches(4.65), Inches(10.5), Inches(0.6), size=13,
           italic=True, color=AMBER)

    # 14 EUI/CEI
    sl = content(prs)
    D.header(sl, "能效標示", "用兩個指標衡量能效", AMBER_MID)
    metrics = [("EUI　用電密度", "ENERGY USE INTENSITY", AMBER,
                ["單位樓地板面積的年用電量", "反映建築物的耗能強度"], "kWh / (m²·年)"),
               ("CEI　碳排密度", "CARBON EMISSION INTENSITY", AMBER_MID,
                ["單位樓地板面積的年碳排量", "反映建築物的碳足跡"], "kgCO₂e / (m²·年)")]
    cw = (Inches(11.53) - Inches(0.28)) / 2
    for i, (h, en, ac, items, unit) in enumerate(metrics):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.2), cw, Inches(2.7), fill=WHITE, line=LINE)
        D.rect(sl, x, Inches(2.2), cw, Pt(2.6), fill=ac)
        D.text(sl, h, x + Inches(0.25), Inches(2.45), cw - Inches(0.4), Inches(0.4),
               size=16, bold=True, color=ac)
        D.text(sl, en, x + Inches(0.25), Inches(2.92), cw - Inches(0.4), Inches(0.3),
               size=9, color=STONE4, font=D.MONO)
        D.bullets(sl, items, x + Inches(0.25), Inches(3.35), cw - Inches(0.5), Inches(1.0),
                  size=12, color=BODY, marker_color=ac, gap=4)
        D.text(sl, unit, x + Inches(0.25), Inches(4.4), cw - Inches(0.4), Inches(0.3),
               size=12, color=ac, font=D.MONO)

    # 15 divider
    D.divider(prs, DARK, "PART 03", "評估系統與範圍",
              "算什麼、算哪些、怎麼算。", AMBER_PALE, AMBER_LG)

    # 16 ECB 六項
    sl = content(prs)
    D.header(sl, "能效計算邊界 ECB", "納入評估的六項耗能", AMBER_MID)
    D.lead(sl, "BERS 以「能效計算邊界（ECB）」界定納入評估的耗能項目，逐一檢視如下六項。",
           y=Inches(1.9), size=13)
    items = [
        dict(accent=AMBER_MID, head="外殼", head_color=AMBER, body="隔熱、遮陽、開窗"),
        dict(accent=AMBER_MID, head="空調", head_color=AMBER, body="主機效率、變頻"),
        dict(accent=AMBER_MID, head="照明", head_color=AMBER, body="LED、智慧控制"),
        dict(accent=AMBER_MID, head="電梯", head_color=AMBER, body="馬達效率、群控調度"),
        dict(accent=AMBER_MID, head="揚水泵", head_color=AMBER, body="給水加壓、屋頂水箱"),
        dict(accent=AMBER_MID, head="機械設備", head_color=AMBER, body="通風、熱水等公共機電"),
    ]
    D.card_row(sl, items[:3], y=Inches(2.85), h=Inches(1.55))
    D.card_row(sl, items[3:], y=Inches(4.6), h=Inches(1.55))

    # 16a-16f EUI 檢核項目逐項說明
    eui_item(prs, 1, "Building Envelope", "外殼", "決定空調負荷的起點",
             ["外牆與屋頂的隔熱性能", "開窗面積、玻璃選用與外遮陽", "朝向配置與開窗位置的優化"],
             "外殼做得好，後面的空調可以用更小的容量，達到一樣的舒適。")
    eui_item(prs, 2, "Air Conditioning", "空調", "通常是最大宗的用電負載",
             ["主機效率（COP／IPLV）", "變頻控制與分區送風", "新風與熱回收設計"],
             "主機效率提高一級，長期電費單上的差異就很可觀。")
    eui_item(prs, 3, "Lighting", "照明", "長時間運轉的固定負載",
             ["燈具發光效率（lm／W）", "公共空間的分區與時段控制", "自然採光與感應控制整合"],
             "走廊、停車場的燈一開就是一整天 —— 效率差一點，全年下來都是電費。")
    eui_item(prs, 4, "Elevators", "電梯", "中高樓層住宅的公共用電大宗",
             ["馬達效率與驅動方式", "待機與低載運轉的能耗控制", "群控調度，減少空跑與等待"],
             "電梯的效率住戶看不到，但每個月的公電費單看得到。")
    eui_item(prs, 5, "Water Pump", "揚水泵", "容易被忽略，卻全天候運轉",
             ["給水加壓與屋頂水箱揚水", "變頻泵與分區減壓設計", "馬達效率與管路損耗"],
             "揚水泵安靜地運轉一整年，是公電費單上常被忽略的一筆。")
    eui_item(prs, 6, "Other Equipment", "機械設備", "把剩下的公共機電都算進去",
             ["地下停車場通風與排風機", "公共空間的熱水系統", "消防、給排水等其餘固定設備"],
             "能效計算邊界把這些細節都納入，標示才貼近建築實際耗能的全貌。")

    # 23 設計策略
    sl = content(prs)
    D.header(sl, "設計策略", "提升能效的兩條路", AMBER_MID)
    D.card_row(sl, [
        dict(accent=AMBER, head="被動式設計", head_color=AMBER,
             body_items=["建築外殼的隔熱與遮陽", "自然採光與自然通風", "座向與開窗的最佳化", "從源頭降低空調與照明需求"]),
        dict(accent=AMBER_MID, head="主動式設計", head_color=AMBER_MID,
             body_items=["高效率空調主機與變頻", "LED 高效照明與智慧控制", "高效率電梯與設備", "再生能源與儲能整合"]),
    ], y=Inches(2.3), h=Inches(2.6))

    # 24 新建vs既有
    sl = content(prs)
    D.header(sl, "評估方式", "新建與既有，算法不同", AMBER_MID)
    D.lead(sl, "手冊依「新建／既有」與建築性質分為多類次系統，對應不同的計算與查證方式。",
           y=Inches(1.95), size=13)
    D.card_row(sl, [
        dict(accent=AMBER, head="新建建築", head_color=AMBER,
             body_items=["以設計圖說做理論計算", "設備與使用情境採標準假設", "屬理論值，不保證等同實際耗能"]),
        dict(accent=AMBER_MID, head="既有建築", head_color=AMBER_MID,
             body_items=["以真實電費單換算、可查證", "可採市場虛擬 EUI 作為基準", "能對照實際營運表現、支援公開揭露"]),
    ], y=Inches(2.85), h=Inches(2.1))
    D.note(sl, "手冊共規範六類次系統的能效標示法；新建為理論計算值，與實際耗能可能有落差。")

    # 25 適用類組
    sl = content(prs)
    D.header(sl, "適用範圍", "幾乎涵蓋各類建築", AMBER_MID)
    D.lead(sl, "2022 年前導版適用 6 類 12 組；2024 年版幾乎適用大部分建築類組，並把所有規定集結"
               "於單一手冊。", y=Inches(1.9), size=13)
    cats = [
        dict(accent=AMBER_MID, head="住宅類", head_color=AMBER, body="H-2 等住宅建築"),
        dict(accent=AMBER_MID, head="文教類", head_color=AMBER, body="D-2 文教設施等"),
        dict(accent=AMBER_MID, head="辦公類", head_color=AMBER, body="辦公與服務業建築"),
        dict(accent=AMBER_MID, head="商業類", head_color=AMBER, body="賣場、餐飲、旅館"),
        dict(accent=AMBER_MID, head="醫療類", head_color=AMBER, body="醫院與照護機構"),
        dict(accent=AMBER_MID, head="其他非住宅", head_color=AMBER, body="多數一般建築類組"),
    ]
    D.card_row(sl, cats[:3], y=Inches(2.8), h=Inches(1.4))
    D.card_row(sl, cats[3:], y=Inches(4.35), h=Inches(1.4))
    D.note(sl, "不適用於特殊廠庫、戒護場所、危險廠庫，及海拔 800 公尺以上等特定類組。")

    # 26 開發案能效目標
    sl = content(prs)
    D.header(sl, "給開發案", "能效目標怎麼設", AMBER_MID)
    D.card_row(sl, [
        dict(accent=AMBER_MID, head="法定門檻", head_color=AMBER, body="至少達主管機關要求的能效等級"),
        dict(accent=AMBER_MID, head="市場定位", head_color=AMBER, body="能效等級對應產品的低碳賣點"),
        dict(accent=AMBER_MID, head="容積策略", head_color=AMBER, body="結合綠建築爭取容積獎勵"),
        dict(accent=AMBER_MID, head="淨零超前", head_color=AMBER, body="朝近零碳 1+ 級超前部署"),
    ], y=Inches(2.4), h=Inches(2.0))
    D.note(sl, "建議規劃初期就設定目標能效等級，再回推外殼、空調、照明與再生能源的規格。")

    # 27 BERS x EEWH
    sl = content(prs)
    D.header(sl, "與綠建築的關係", "BERS 與綠建築，分進合擊", AMBER_MID)
    D.lead(sl, "綠建築 EEWH 的「日常節能指標」可採建築能效評估法，直接以 BERS 的得分換算 —— "
               "兩套制度彼此銜接、互相加分。", y=Inches(1.95))
    cw = (Inches(11.53) - Inches(0.28)) / 2
    D.rect(sl, Inches(0.9), Inches(3.3), cw, Inches(1.9), fill=WHITE, line=LINE)
    D.rect(sl, Inches(0.9), Inches(3.3), cw, Pt(2.6), fill="#064e3b")
    D.text(sl, "綠建築 EEWH", Inches(1.15), Inches(3.55), cw - Inches(0.4), Inches(0.4),
           size=15, bold=True, color="#064e3b")
    D.bullets(sl, ["四大範疇、九大指標", "日常節能可採建築能效法計分"],
              Inches(1.15), Inches(4.1), cw - Inches(0.5), Inches(1.0), size=12,
              color=BODY, marker_color="#064e3b", gap=4)
    x2 = Inches(0.9) + cw + Inches(0.28)
    D.rect(sl, x2, Inches(3.3), cw, Inches(1.9), fill=AMBER)
    D.text(sl, "建築能效 BERS", x2 + Inches(0.25), Inches(3.55), cw - Inches(0.4), Inches(0.4),
           size=15, bold=True, color=WHITE)
    D.bullets(sl, ["量化能效、產生能效得分", "回饋綠建築的日常節能評分"],
              x2 + Inches(0.25), Inches(4.1), cw - Inches(0.5), Inches(1.0), size=12,
              color=WHITE, marker_color=AMBER_PALE, gap=4)

    # 28 divider
    D.divider(prs, DARK, "PART 04", "對開發案與淨零",
              "能效不只是標示，更是政策門檻。", AMBER_PALE, AMBER_LG)

    # 29 政策強制要求
    sl = content(prs)
    D.header(sl, "從鼓勵到強制", "能效已成為法定門檻", AMBER_MID)
    D.lead(sl, "建築能效正從「鼓勵」走向「強制」，是開發案必須提前因應的政策。", y=Inches(1.95), size=13)
    pol = [("2030", AMBER, "公有新建建築", "須達能效 1 級或近零碳建築"),
           ("2040", AMBER_MID, "既有建築更新", "50% 更新為能效 1 級或近零碳"),
           ("2050", "#92400e", "全面近零碳", "100% 新建、逾 85% 為近零碳")]
    cw = (Inches(11.53) - Inches(0.28) * 2) / 3
    for i, (yr, ac, h, b) in enumerate(pol):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.85), cw, Inches(2.0), fill=WHITE, line=LINE)
        D.rect(sl, x, Inches(2.85), cw, Pt(2.6), fill=ac)
        D.text(sl, yr, x + Inches(0.25), Inches(3.05), cw - Inches(0.4), Inches(0.6),
               size=26, bold=True, color=ac)
        D.text(sl, h, x + Inches(0.25), Inches(3.7), cw - Inches(0.4), Inches(0.4),
               size=14, bold=True, color=CHAR)
        D.text(sl, b, x + Inches(0.25), Inches(4.15), cw - Inches(0.4), Inches(0.6),
               size=11.5, color=BODY, spacing=1.2)
    D.note(sl, "實際適用範圍與時程，依主管機關最新法令與公告為準。")

    # 30 能效作為產品價值
    sl = content(prs)
    D.header(sl, "產品價值", "能效，是碳資產也是賣點", AMBER_MID)
    D.card_row(sl, [
        dict(accent=AMBER_MID, head="對住戶", head_color=AMBER,
             body_items=["高能效代表長期電費實際降低", "能效標示是看得懂的低碳保證"]),
        dict(accent=AMBER_MID, head="對開發", head_color=AMBER,
             body_items=["可結合綠建築爭取容積獎勵", "提前布局，避開未來的法規門檻風險"]),
    ], y=Inches(2.3), h=Inches(1.9))
    D.rect(sl, Inches(0.9), Inches(4.6), Pt(2), Inches(0.6), fill=AMBER_LG)
    D.text(sl, "在淨零成為市場語言的當下，高能效既是產品的差異化賣點，也是長期保值的籌碼。",
           Inches(1.1), Inches(4.65), Inches(10.5), Inches(0.6), size=13,
           italic=True, color=AMBER)

    # 31 三標章整合
    sl = content(prs)
    D.header(sl, "標章整合", "綠建築 × 智慧 × 能效", AMBER_MID)
    D.lead(sl, "三套標章彼此呼應、可合併申請，共同支撐淨零建築與開發效益。", y=Inches(1.95), size=13)
    cw = (Inches(11.53) - Inches(0.28) * 2) / 3
    trio = [("綠建築 EEWH", "#064e3b", "生態、節能、減廢、健康", None),
            ("智慧建築", "#1e40af", "偵知、顯示、連動的智慧化", None),
            ("建築能效 BERS", AMBER, "量化能效，邁向近零碳", AMBER)]
    for i, (h, ac, b, fillc) in enumerate(trio):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        if fillc:
            D.rect(sl, x, Inches(2.9), cw, Inches(1.8), fill=fillc)
            hc, bc = WHITE, "#fef3c7"
        else:
            D.rect(sl, x, Inches(2.9), cw, Inches(1.8), fill=WHITE, line=LINE)
            D.rect(sl, x, Inches(2.9), cw, Pt(2.6), fill=ac)
            hc, bc = ac, BODY
        D.text(sl, h, x + Inches(0.25), Inches(3.2), cw - Inches(0.4), Inches(0.4),
               size=15, bold=True, color=hc)
        D.text(sl, b, x + Inches(0.25), Inches(3.75), cw - Inches(0.4), Inches(0.6),
               size=11.5, color=bc, spacing=1.2)

    # 32 申請流程
    sl = content(prs)
    D.header(sl, "申請流程", "從計算到取得標示", AMBER_MID)
    steps = [("01", "能效計算", "依 ECB 計算 EUI／CEI 與能效分數"),
             ("02", "候選證書", "新建以設計圖說申請能效評估"),
             ("03", "查核確認", "施工落實，文件查驗"),
             ("04", "能效標示", "完工取得 1+ 至 7 級標示，公開揭露")]
    cw = (Inches(11.53) - Inches(0.28) * 3) / 4
    for i, (n, h, b) in enumerate(steps):
        x = Inches(0.9) + (cw + Inches(0.28)) * i
        D.rect(sl, x, Inches(2.6), cw, Inches(2.1), fill=WHITE, line=LINE)
        D.text(sl, n, x + Inches(0.22), Inches(2.82), cw - Inches(0.4), Inches(0.3),
               size=11, color=AMBER, font=D.MONO)
        D.text(sl, h, x + Inches(0.22), Inches(3.2), cw - Inches(0.4), Inches(0.4),
               size=14, bold=True, color=CHAR)
        D.text(sl, b, x + Inches(0.22), Inches(3.7), cw - Inches(0.4), Inches(0.9),
               size=11, color=BODY, spacing=1.25)

    # 33 BERS vs EEWH table
    sl = content(prs)
    D.header(sl, "兩者差異", "建築能效 與 綠建築 有何不同", AMBER_MID)
    rows = [("關注面向", "生態／節能／減廢／健康，綜合環境評估", "專注於能源效率單一面向"),
            ("衡量方式", "四大範疇、九大指標", "量化 EUI／CEI 並分級"),
            ("分級", "鑽石至合格，共五級", "1+ 至 7，共七階段"),
            ("目標", "整體環境品質", "對接近零碳建築")]
    cols = [(Inches(0.9), Inches(2.0)), (Inches(2.95), Inches(4.6)), (Inches(7.65), Inches(4.78))]
    hy = Inches(2.3)
    heads = [("", STONE4), ("綠建築 EEWH", "#064e3b"), ("建築能效 BERS", AMBER)]
    for (cx, cwd), (htext, hc) in zip(cols, heads):
        if htext:
            D.text(sl, htext, cx, hy, cwd, Inches(0.4), size=13, bold=True, color=hc)
    D.rect(sl, Inches(0.9), hy + Inches(0.5), Inches(11.53), Pt(1.5), fill="#d6d3d1")
    ry = hy + Inches(0.65)
    for k, a, b in rows:
        D.text(sl, k, cols[0][0], ry, cols[0][1], Inches(0.6), size=12, color=STONE4)
        D.text(sl, a, cols[1][0], ry, cols[1][1], Inches(0.7), size=12, color=BODY, spacing=1.15)
        D.text(sl, b, cols[2][0], ry, cols[2][1], Inches(0.7), size=12, color=BODY, spacing=1.15)
        D.rect(sl, Inches(0.9), ry + Inches(0.72), Inches(11.53), Pt(0.75), fill=LINE)
        ry += Inches(0.88)
    D.note(sl, "兩者相輔相成：綠建築看整體環境、建築能效專精能源，且可互相換算。")

    # 34 重點回顧
    sl = content(prs)
    D.header(sl, "重點回顧", "關於 BERS，記住這幾點", AMBER_MID)
    D.bullets(sl, [
        "BERS 把建築能效「量化、分級、標示」，制度仿自歐盟 EPBD",
        "七階段分級 1+ 到 7，以市場平均能效為合格分界",
        "1+ 為近零碳建築：住宅減碳 30% 以上、非住宅節能 50% 以上",
        "計算邊界 ECB 涵蓋外殼、空調、照明、電梯、揚水泵與機械設備",
        "標示以 EUI（用電密度）或 CEI（碳排密度）呈現",
        "對接 2050 淨零：2030 年起公有新建須達能效 1 級或近零碳",
    ], Inches(0.9), Inches(2.1), Inches(11.3), Inches(3.5), size=14, color=BODY,
        marker_color=AMBER_MID, gap=9, spacing=1.2)

    # 35 closing
    D.closing(prs, DARK, "BERS ｜ 量化能效・邁向淨零",
              "把能效講清楚，\n讓淨零看得見", AMBER_LG)

    prs.save(path)
    print(f"saved {path} · {len(prs.slides._sldIdLst)} slides")


if __name__ == "__main__":
    build("/home/user/jieceng-web/presentation-BERS.pptx")
