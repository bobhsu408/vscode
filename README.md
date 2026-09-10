# VS Code 入門三小時 — 課程教材

給零程式背景學員的 3 小時 VS Code 教學課程，包含講義、投影片與實作用的授權教學靶機。

## 內容

| 檔案 | 說明 |
|---|---|
| [vscode-course.html](vscode-course.html) | 講義網頁（可直接投影或部署到自己的伺服器） |
| [vscode-course-notes.md](vscode-course-notes.md) | 講師備課教案筆記，逐時段帶教技巧 |
| [vscode-course.pptx](vscode-course.pptx) | 投影片（由 `build_ppt.py` 產生） |
| [build_ppt.py](build_ppt.py) | PPT 產生腳本，需 `python-pptx` |
| [checkin-target/](checkin-target/) | 實作用的簽到靶機（Docker + FastAPI） |

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
| 02:25–02:45 | 整合終端機與 Git 基礎 |
| 02:45–03:00 | 實作：簽到靶機 API 練習 |

> 教學順序邏輯：安裝後先讓學員動手做「有感」的事（開自己的檔案、換喜歡的顏色），累積成就感後才進入偏理論的介面導覽。

## 重新產生投影片

```bash
pip install python-pptx
python3 build_ppt.py
```

## 啟動教學靶機

```bash
cd checkin-target
docker compose up --build
```

前端頁面 http://localhost:8000/ ，API 文件 http://localhost:8000/docs

## 授權說明

`checkin-target/` 是**刻意不實作身分驗證**的教學靶機，用於示範 API 缺少授權驗證的風險（對應 OWASP API Security Top 10 的 API2：Broken Authentication）。僅供授權範圍內的課程教學使用，請勿對外公開部署。
