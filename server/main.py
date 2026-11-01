from fastapi import FastAPI, Request

app = FastAPI(title="Notion Sync")

TOOLS = [
    {
        "name": "search_pages",
        "description": "Найти страницы по запросу",
        "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]},
    }
]


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "notion-sync"}


@app.post("/mcp")
async def mcp(request: Request) -> dict:
    body = await request.json()
    if body.get("method") == "tools/list":
        return {"jsonrpc": "2.0", "id": body.get("id"), "result": {"tools": TOOLS}}
    if body.get("method") == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "notion-sync", "version": "1.0.0"},
            },
        }
    return {"jsonrpc": "2.0", "id": body.get("id"), "error": {"code": -32601, "message": "Method not found"}}
