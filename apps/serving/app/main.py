from fastapi import FastAPI

app = FastAPI(title="MCP Serving API")

@app.get("/infer")
def infer():
    return {"prediction": "dummy"}
