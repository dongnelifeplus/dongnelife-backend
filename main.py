from fastapi import FastAPI
import os

app = FastAPI()

# 1. 정책 데이터 수신 API
@app.post("/ingest/policies")
def ingest_policies(data: list):
    # 데이터 수신 시 분석 시작
    return {"status": "success", "message": f"{len(data)}건의 행복 데이터 수신 완료!"}

# 2. 서버 상태 확인
@app.get("/")
def read_root():
    return {"status": "행복이 엔진 가동 중! 🐷"}