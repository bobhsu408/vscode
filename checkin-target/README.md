# 課程簽到系統（教學靶機）

**用途**：VS Code 課程「簽到靶機 API 練習」單元用的授權教學靶機。故意不做任何登入/token 驗證，用於示範 API 缺少授權驗證（對應 OWASP API Security Top 10 的 API2：Broken Authentication / Missing Access Control）。

僅供講師自己架設、授權範圍內的課程練習使用，請勿對外公開部署或用於未授權對象。

## 啟動方式（Docker）

```bash
cd checkin-target
docker compose up --build
```

啟動後：

- 前端頁面：http://localhost:8000/
- API 文件（Swagger UI）：http://localhost:8000/docs

停止：

```bash
docker compose down
```

## API 一覽

| 端點 | 方法 | 參數 | 說明 |
|---|---|---|---|
| `/api/checkin` | POST | `{"user_id": "student01"}` | 簽到，無需驗證 |
| `/api/checkout` | POST | `{"user_id": "student01"}` | 簽退，無需驗證 |
| `/api/records` | GET | — | 查詢所有人簽到狀態與歷史 |
| `/api/records/{user_id}` | GET | — | 查詢單一學員紀錄 |

## 預置學員帳號

`student01` ~ `student05`（皆為假資料，對應中文姓名如王小明、陳小美…）。

## 課堂使用建議

1. 先帶學員開 `/docs`，用 Swagger 內建「Try it out」手動呼叫一次 `checkin`，觀察不需登入就能成功。
2. 開前端頁面 `/`，即時看到簽到狀態變化（3 秒自動刷新）。
3. 再帶學員寫 `checkin.py` 用 `requests` 呼叫同樣的 API。
4. 收尾討論：因為沒有驗證身分，任何人可以代替別人簽到/簽退，且 `/docs` 直接曝露了所有可呼叫端點——這就是本練習要示範的風險。

## 重置資料

資料存在記憶體中，重啟容器即可清空回到初始狀態：

```bash
docker compose restart
```
