from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
BASE_DIR = Path(__file__).parent


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/api/status")
def status():
    return {
        "status": "working",
        "message": "hello from server",
        "server_time_utc": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/greet/{name}")
def greet(name: str):
    return {"message": f"أهلاً يا {name} 👋 من السيرفر"}


@app.get("/health")
def health():
    return {"ok": True}