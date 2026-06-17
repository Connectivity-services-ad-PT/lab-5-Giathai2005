import os
import requests
import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI(title="IoT Ingestion Gateway")

# Đọc cấu hình từ biến môi trường do Docker Compose cấp
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
AI_HOST = os.getenv("AI_SERVICE_HOST", "localhost")

def check_db():
    try:
        conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, dbname=DB_NAME, connect_timeout=2)
        conn.close()
        return True
    except:
        return False

def check_ai():
    try:
        res = requests.get(f"http://{AI_HOST}:9000/health", timeout=2)
        return res.status_code == 200
    except:
        return False

@app.get("/health")
def health_check():
    db_status = check_db()
    ai_status = check_ai()
    
    if db_status and ai_status:
        return {"status": "healthy", "database": "connected", "ai_service": "connected"}
    
    raise HTTPException(
        status_code=503,
        detail={"status": "unhealthy", "database": "OK" if db_status else "FAIL", "ai_service": "OK" if ai_status else "FAIL"}
    )