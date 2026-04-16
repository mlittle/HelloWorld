from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["default"])
def read_root():
    return {"message": "hello world"}

@app.get("/health", tags=["health"])
def read_health():
    return {"status": "ok"}
