from fastapi import FastAPI
import os
import uvicorn

app = FastAPI(title="Test MCP Server")

@app.get("/mcp/tools")
async def list_tools():
    return {
        "tools": [
            {
                "name": "ping",
                "description": "Connectivity test",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    }

@app.post("/mcp/tools/ping")
async def ping():
    return {
        "type": "text",
        "text": "pong"
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "test123:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )
