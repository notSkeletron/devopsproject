from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/hello", response_class=PlainTextResponse)
async def say_hello():
    return "Hello, World!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)