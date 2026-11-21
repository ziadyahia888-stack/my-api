from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


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