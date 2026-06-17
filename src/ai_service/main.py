import time
from fastapi import FastAPI, HTTPException

app = FastAPI(title="AI Service - Team IoT")
MODEL_READY = False

@app.on_event("startup")
def load_model():
    global MODEL_READY
    time.sleep(3)  # Giả lập thời gian load weight của mô hình
    MODEL_READY = True
    print("🤖 AI Model loaded and ready!")

@app.get("/health")
def health_check():
    if not MODEL_READY:
        raise HTTPException(status_code=503, detail="AI Model is loading...")
    return {"status": "healthy", "model": "Mock-YOLOv8"}

@app.post("/predict")
def predict(payload: dict):
    if not MODEL_READY:
        raise HTTPException(status_code=503, detail="Model not ready")
    return {"prediction": "object_detected", "confidence": 0.95}