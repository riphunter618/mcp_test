from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()


@app.post("/")
async def root():
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


@app.post("/ping")
async def ping():
    return {
        "content": [
            {"type": "text", "text": "pong"}
        ]
    }


if __name__ == "__main__":
    # Use the PORT environment variable Render provides, fallback to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("test123:app", host="0.0.0.0", port=port, reload=True)
