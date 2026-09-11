# -*- coding: utf-8 -*-
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

INK = RGBColor(0x1E, 0x1E, 0x2E)
STEEL = RGBColor(0x3D, 0x5A, 0x80)
AMBER = RGBColor(0xC8, 0x86, 0x3A)
GREY = RGBColor(0x6B, 0x72, 0x80)
PAPER = RGBColor(0xF7, 0xF6, 0xF3)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

def add_bg(slide, color=PAPER):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color

def add_textbox(slide, left, top, width, height):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tb.text_frame.word_wrap = True
    return tb

def set_run(run, text, size, color, bold=False, font="Microsoft JhengHei"):
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = font

def title_slide(title, subtitle, tag):
    slide = prs.slides.add_slide(blank)
    add_bg(slide)
    # accent bar
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.18), prs.slide_height)
    bar.fill.solid(); bar.fill.fore_color.rgb = STEEL
    bar.line.fill.background()

    tb = add_textbox(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(0.5))
    p = tb.text_frame.paragraphs[0]
    r = p.add_run(); set_run(r, tag, 14, STEEL, bold=True)

    tb2 = add_textbox(slide, Inches(0.8), Inches(1.1), Inches(11.5), Inches(1.6))
    p2 = tb2.text_frame.paragraphs[0]
    r2 = p2.add_run(); set_run(r2, title, 40, INK, bold=True)

    tb3 = add_textbox(slide, Inches(0.8), Inches(2.3), Inches(11), Inches(1.5))
    p3 = tb3.text_frame.paragraphs[0]
    r3 = p3.add_run(); set_run(r3, subtitle, 18, GREY)
    return slide

def content_slide(tag, heading, bullets, note=None, note_color=STEEL, code=None):
    slide = prs.slides.add_slide(blank)
    add_bg(slide)
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.18), prs.slide_height)
    bar.fill.solid(); bar.fill.fore_color.rgb = STEEL
    bar.line.fill.background()

    tb = add_textbox(slide, Inches(0.8), Inches(0.45), Inches(11), Inches(0.4))
    p = tb.text_frame.paragraphs[0]
    r = p.add_run(); set_run(r, tag, 13, STEEL, bold=True)

    tb2 = add_textbox(slide, Inches(0.8), Inches(0.85), Inches(11.5), Inches(0.9))
    p2 = tb2.text_frame.paragraphs[0]
    r2 = p2.add_run(); set_run(r2, heading, 30, INK, bold=True)

    top = 1.9
    if bullets:
        tb3 = add_textbox(slide, Inches(0.9), Inches(top), Inches(11.2), Inches(3.6))
        tf = tb3.text_frame
        for i, b in enumerate(bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(10)
            r = p.add_run(); set_run(r, "•  " + b, 18, INK)
        top += 0.5 * len(bullets) + 0.6

    if code:
        code_box = slide.shapes.add_shape(1, Inches(0.9), Inches(top), Inches(11.2), Inches(1.6))
        code_box.fill.solid(); code_box.fill.fore_color.rgb = INK
        code_box.line.fill.background()
        tf = code_box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.15)
        for i, line in enumerate(code):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            r = p.add_run(); set_run(r, line, 14, RGBColor(0xD4,0xD4,0xDC), font="Consolas")
        top += 1.9

    if note:
        note_box = slide.shapes.add_shape(1, Inches(0.9), Inches(top), Inches(11.2), Inches(0.9))
        note_box.fill.solid(); note_box.fill.fore_color.rgb = RGBColor(0xE8,0xEE,0xF4) if note_color==STEEL else RGBColor(0xF6,0xE9,0xD8)
        note_box.line.fill.background()
        tf = note_box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.12)
        p = tf.paragraphs[0]
        r = p.add_run(); set_run(r, note, 15, note_color, bold=True)
    return slide

# 1. Cover
title_slide(
    "VS Code 入門三小時",
    "從零安裝到能寫、能跑、能用終端機與 Git 的基本工作流。\n對象：有基礎電腦操作,未寫過程式。",
    "課程教案 · 逐時段講義"
)

# 2. Agenda
content_slide("00:00 起", "今天的路線圖", [
    "00:00–00:20  安裝與初次啟動",
    "00:20–00:45  檔案與專案管理：打開下載資料夾與講義文件",
    "00:45–01:05  換主題、換字型",
    "01:05–01:15  繁體中文化（可選）",
    "01:15–01:40  介面認識",
    "01:40–01:50  休息",
    "01:50–02:15  編輯技巧與快捷鍵",
    "02:15–02:25  擴充套件：安裝 Python",
    "02:25–02:45  終端機、寫一支程式執行、Git 基礎",
    "02:45–03:00  實作：做一張自己的個人名片網頁",
])

# 3. Install
content_slide("00:00–00:15", "下載與安裝", [
    "官網下載對應版本（Windows .exe / macOS .zip）",
    "強調：這是編輯器，不是瀏覽器",
    "Windows 安裝時勾選「加入右鍵選單」「加入 PATH」",
    "常見卡點：無系統管理員權限 → 使用者層級安裝版",
], note="現場提示：全程跟做，不要用投影帶過——這一步最容易個別卡住", note_color=STEEL)

# 4. First launch
content_slide("00:15–00:20", "初次啟動一覽", [
    "語言暫時保持英文，介面認識與中文化留到後面模組",
    "示範一次 Ctrl+Shift+P（Mac：Cmd+Shift+P）開啟命令面板",
    "讓學員有印象即可，不深入教",
])

# 5. Folder = Project
content_slide("00:20–00:30", "「開啟資料夾」＝ VS Code 裡的專案", [
    "VS Code 沒有「新建專案」按鈕",
    "File → Open Folder，選取「下載」資料夾",
    "課程講義 PPT / 文件已預先透過課程網頁提供下載",
    "左側 Explorer 顯示該資料夾內容",
])

# 6. Office viewer extension
content_slide("00:30–00:45", "用 Office 擴充套件直接看 PPT / Word", [
    "Extensions 面板搜尋安裝 Office Viewer 類套件",
    "點開課程講義 PPT，直接在分頁裡翻頁預覽",
    "不需要另外開 PowerPoint",
    "順便示範開啟一個 .docx 講義文件比對",
], note="帶學員做：請每個人自己在下載資料夾裡找到今天的講義並點開看一次", note_color=STEEL)

# 6b. File ops
content_slide("00:40–00:45", "建立、儲存檔案小練習", [
    "右鍵 Explorer 空白處 → New File，練習新建空白 .txt",
    "存檔快捷鍵 Ctrl+S；分頁圓點代表尚未儲存",
], note="常見誤解：學員常以為要「存專案」，其實只存個別檔案，資料夾只是視窗顯示範圍", note_color=AMBER)

# 7. Theme customization
content_slide("00:45–00:55", "切換色彩主題", [
    "命令面板 → Preferences: Color Theme（方向鍵即時預覽）",
    "命令面板 → Preferences: File Icon Theme",
    "可額外安裝主題套件（如 One Dark Pro）擴充選擇",
], note="帶學員做：讓每個人選一個喜歡的主題，鼓勵現場分享畫面，順便複習命令面板", note_color=STEEL)

# 8. Font size
content_slide("00:55–01:05", "調整字型大小與字體", [
    "設定搜尋 font size 調整編輯字型大小",
    "設定搜尋 font family 調整字體",
    "示範放大字型對長時間閱讀程式碼的幫助",
])

# 9. Localization (optional)
content_slide("01:05–01:15", "繁體中文化（可選）", [
    "介面已經玩過一輪、顏色也換好了，讓學員自行決定是否切換",
    "命令面板輸入 Configure Display Language",
    "安裝 Chinese (Traditional) Language Pack，重啟生效",
], note="不強制統一語言：投影示範用中文介面，學員機器保留英文也沒問題", note_color=STEEL)

# 10. Interface tour
content_slide("01:15–01:25", "介面五大分區", [
    "Activity Bar（左側最窄那排圖示）：切換功能面板",
    "側邊欄：檔案總管、搜尋、原始碼控制、擴充套件",
    "編輯區：真正打字的地方，可分割成多個分頁/窗格",
    "狀態列（底部）：語言、編碼、游標位置、Git 分支",
    "右上角工具列：分割編輯器、開啟終端機、切換版面",
])

# 11. Menu bar
content_slide("01:25–01:40", "最上方選單列（File / Edit / View…）", [
    "跟命令面板是兩條通往同樣功能的路，更適合「用滑鼠慢慢找」",
    "File：Open Folder、Save、Save As",
    "View：開啟 Explorer、Terminal、Extensions 等面板",
    "Run：執行目前開啟的檔案，等一下寫小程式時也能從這裡跑",
], note="視窗變窄時選單列會摺疊成「⋯」（More Actions）圖示，收進 Terminal、Help 等選項——別以為選單不見了", note_color=AMBER)

# 12. Break
title_slide("休息 10 分鐘", "01:40 – 01:50", "☕ BREAK")

# 13. Multi-cursor
content_slide("01:50–02:02", "多游標與搜尋取代", [
    "Alt（Mac：Option）+ 點擊多處，同時打字",
    "Ctrl+D 選取下一個相同字詞，連續按可多選",
    "Ctrl+F 尋找、Ctrl+H 取代",
    "Ctrl+Shift+F 跨整個專案搜尋",
])

# 14. Shortcuts
content_slide("02:02–02:15", "常用快捷鍵小抄", [
    "命令面板：Ctrl+Shift+P",
    "快速切換檔案：Ctrl+P",
    "開啟／收起終端機：Ctrl+`",
    "複製整行：Shift+Alt+↓",
    "單行註解：Ctrl+/",
    "分割編輯器：Ctrl+\\",
    "格式化文件：Shift+Alt+F",
])

# 15. Extensions
content_slide("02:15–02:25", "擴充套件：安裝 Python", [
    "主題、字型、中文包已在課程一開頭裝過",
    "Activity Bar 中方塊圖示 → Extensions",
    "安裝 Python（Microsoft 官方）：等下要寫一支小程式來執行",
    "示範停用 / 解除安裝套件的差異",
])

# 16. Terminal
content_slide("02:25–02:31", "內建終端機", [
    "Ctrl+` 開啟整合終端機——在目前資料夾底下開的命令列",
], note="常見卡點：Windows 上可能要打 py；macOS 上可能要打 python3。上課前務必實測學員機型", note_color=AMBER,
code=[
    "python --version",
    "cd Desktop/vscode-workshop",
    "dir   # macOS 用 ls",
])

# 16b. Write and run a program
content_slide("02:31–02:39", "寫一支程式並執行", [
    "新建 game.py，帶學員一行一行打完",
    "終端機執行 python game.py",
], note="第一次體驗「我寫的東西跑起來了」。程式要短到每個人都打得完，不是看老師打字", note_color=STEEL,
code=[
    "import random",
    "",
    "a = random.randint(1, 50)",
    "b = random.randint(1, 50)",
    "",
    'print(f"{a} + {b} = ?")',
    'answer = int(input("你的答案："))',
    "",
    "if answer == a + b:",
    '    print("答對了！")',
    "else:",
    '    print(f"答錯囉～ 正確答案是 {a + b}")',
])

# 17. Git basics
content_slide("02:39–02:45", "Git 基礎操作", [
    "終端機輸入 git init 初始化版本控制",
    "編輯檔案後，左側「原始碼控制」圖示會顯示變更數量",
    "訊息框輸入說明文字，Ctrl+Enter 完成 commit",
], note="教學用意：不深入教 Git 指令，只讓學員知道「存檔的存檔」這個概念存在", note_color=STEEL)

# 18. Card exercise intro
content_slide("02:45–02:49", "實作：做一張自己的個人名片網頁", [
    "Explorer 右鍵 → New File，檔名整串連 .html 一起打：card.html",
    "從課程網頁複製模板全文，Ctrl+V 貼上，Ctrl+S 存檔",
    "先用瀏覽器打開看一眼成品，再開始改",
], note="不需要網路、不需要安裝任何東西——刻意設計成不可能失敗，因為它是學員帶走的最後印象", note_color=STEEL)

# 19. Three editing techniques
content_slide("02:50–02:58", "三個編輯技巧，一次用上", [
    "Ctrl+D 換名字：連按選起全部 3 處，一次改完",
    "Alt+點擊 改三個技能標籤：三個游標同時打字",
    "Ctrl+H 換主題色：找 #3D5A80，確認「找到 5 筆」後全部取代",
], note="常見誤解：多游標不是複製貼上三次，是三個游標同時打同樣的字。按過頭用 Ctrl+U 退回", note_color=AMBER)

# 20. Wrap up
content_slide("02:58–03:00", "回瀏覽器看成果", [
    "填完自我介紹、身分、Email、城市，Ctrl+S 存檔",
    "切回瀏覽器按 F5——那是你自己的一頁",
    "收尾：你不是學會寫網頁，是學會用 VS Code 快速改一份檔案",
], note="鼓勵學員轉螢幕給旁邊的人看，比照換主題那段的分享節奏", note_color=STEEL)

# 22. Checklist
content_slide("課後", "自我檢查清單", [
    "能獨立安裝 VS Code",
    "能開啟資料夾，並用 Office 擴充套件直接瀏覽 PPT / Word 文件",
    "能切換喜歡的色彩主題與字型，依個人習慣決定是否切換為繁體中文",
    "能講出五大介面分區與選單列的用途，並用命令面板找到任何功能",
    "能使用多游標與搜尋取代加速編輯",
    "能安裝擴充套件（Python）並開啟整合終端機執行基本指令",
    "能寫出一支簡單的 Python 程式並在終端機執行",
    "能新建 HTML 檔案、用多游標與搜尋取代完成一份自己的作品，並在瀏覽器打開它",
])

out_path = "/media/data/共用文件/專案開發/微軟大戰程式碼/vscode-course.pptx"
prs.save(out_path)
print("saved:", out_path)
