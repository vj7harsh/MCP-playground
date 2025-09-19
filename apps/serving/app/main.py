from fastapi import FastAPI

app = FastAPI(title="MCP Serving API")

# uvicorn app.main:app --reload

@app.get("/infer")
def infer():
    return {"prediction": "dummy"}
