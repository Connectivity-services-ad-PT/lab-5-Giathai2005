from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai"}

@app.post("/predict")
def predict():
    return {
        "objects": ["person", "bicycle"],
        "confidence": [0.98, 0.85]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)