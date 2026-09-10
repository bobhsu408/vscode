from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(
    title="課程簽到系統（教學靶機）",
    description=(
        "本系統僅供 VS Code 課程之授權資安教學使用。\n\n"
        "**注意：本系統故意未實作任何登入驗證，任何人皆可呼叫 /api 下所有端點。**"
    ),
    version="1.0.0",
)

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 預置假學員資料
STUDENTS = {
    "student01": "王小明",
    "student02": "陳小美",
    "student03": "林大華",
    "student04": "張小芳",
    "student05": "李阿強",
}

# 記憶體內簽到紀錄： user_id -> {"status": "in"/"out", "history": [...]}
records: dict[str, dict] = {
    uid: {"status": "out", "history": []} for uid in STUDENTS
}


class CheckRequest(BaseModel):
    user_id: str


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _ensure_known(user_id: str) -> None:
    if user_id not in STUDENTS:
        raise HTTPException(status_code=404, detail=f"未知的學員 user_id: {user_id}")


@app.post("/api/checkin")
def checkin(req: CheckRequest):
    """簽到 — 故意不驗證身分，任何人皆可代任意 user_id 簽到。"""
    _ensure_known(req.user_id)
    record = records[req.user_id]
    record["status"] = "in"
    record["history"].append({"action": "checkin", "time": _now()})
    return {
        "user_id": req.user_id,
        "name": STUDENTS[req.user_id],
        "status": "in",
        "time": record["history"][-1]["time"],
    }


@app.post("/api/checkout")
def checkout(req: CheckRequest):
    """簽退 — 同樣未驗證身分。"""
    _ensure_known(req.user_id)
    record = records[req.user_id]
    record["status"] = "out"
    record["history"].append({"action": "checkout", "time": _now()})
    return {
        "user_id": req.user_id,
        "name": STUDENTS[req.user_id],
        "status": "out",
        "time": record["history"][-1]["time"],
    }


@app.get("/api/records")
def list_records():
    """查詢所有人的簽到狀態與歷史紀錄 — 無需登入即可看到所有人資料。"""
    return [
        {
            "user_id": uid,
            "name": name,
            "status": records[uid]["status"],
            "history": records[uid]["history"],
        }
        for uid, name in STUDENTS.items()
    ]


@app.get("/api/records/{user_id}")
def get_record(user_id: str):
    """查詢單一學員的簽到紀錄。"""
    _ensure_known(user_id)
    return {
        "user_id": user_id,
        "name": STUDENTS[user_id],
        **records[user_id],
    }


@app.get("/", response_class=HTMLResponse)
def index():
    return (STATIC_DIR / "index.html").read_text(encoding="utf-8")
