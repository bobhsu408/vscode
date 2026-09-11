# VS Code 入門三小時 — 課程教材

給零程式背景學員的 3 小時 VS Code 教學課程，包含講義、投影片與兩段動手實作。

## 內容

| 檔案 | 說明 |
|---|---|
| [site/content/index.html](site/content/index.html) | 講義網頁（可直接投影或部署到自己的伺服器） |
| [vscode-course-notes.md](vscode-course-notes.md) | 講師備課教案筆記，逐時段帶教技巧 |
| [site/content/vscode-course.pptx](site/content/vscode-course.pptx) | 投影片（由 `build_ppt.py` 產生） |
| [build_ppt.py](build_ppt.py) | PPT 產生腳本，需 `python-pptx` |
| [site/content/card-template.html.txt](site/content/card-template.html.txt) | 最後實作用的個人名片模板 |
| [game.py](game.py) | 終端機模組帶學員手寫的小程式 |
| [game-extended.py](game-extended.py) | 同一個想法的完整版，給提早做完的學員參考 |

## 課程流程

| 時段 | 模組 |
|---|---|
| 00:00–00:20 | 安裝與初次啟動 |
| 00:20–00:45 | 檔案與專案管理（Open Folder + Office 擴充套件瀏覽 PPT/Word） |
| 00:45–01:05 | 換主題、換字型 |
| 01:05–01:15 | 繁體中文化（可選） |
| 01:15–01:40 | 介面認識（五大分區 + 選單列） |
| 01:40–01:50 | 休息 |
| 01:50–02:15 | 編輯技巧與快捷鍵 |
| 02:15–02:25 | 擴充套件：安裝 Python |
| 02:25–02:45 | 終端機、寫一支程式執行、Git 基礎 |
| 02:45–03:00 | 實作：做一張自己的個人名片網頁 |

> 教學順序邏輯：安裝後先讓學員動手做「有感」的事（開自己的檔案、換喜歡的顏色），累積成就感後才進入偏理論的介面導覽。

## 重新產生投影片

```bash
pip install python-pptx
python3 build_ppt.py
```

## 兩段實作

**02:25–02:45　寫一支程式並執行**
學員在終端機新建 `game.py`（約 10 行，見 [game.py](game.py)）並跑起來，第一次體驗「我寫的東西跑起來了」。`game-extended.py` 是完整版，只給提早做完的學員參考，不要求當場打完。

**02:45–03:00　做一張個人名片網頁**
學員新建 `card.html`，貼上 [模板](site/content/card-template.html.txt)，用 `Ctrl+D`、`Alt`+點擊、`Ctrl+H` 把它改成自己的，存檔後用瀏覽器打開。**零網路、零安裝**——模板刻意讓前面教過的編輯技巧成為最省力的解法（`你的名字` 重複 3 處、主題色 `#3D5A80` 重複 5 處、三個同構的技能標籤）。

模板透過課程網頁以 `<pre>` 提供學員複製，而不是給下載連結：`.html` 放上網站會被瀏覽器渲染而非下載，右鍵另存很容易存成 `.htm` 或整頁封存目錄。改成手動新建，副檔名由學員親手打出來。
