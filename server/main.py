from fastapi import FastAPI

app = FastAPI(title="Notion Sync")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "notion-sync"}
