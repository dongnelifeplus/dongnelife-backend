from fastapi import FastAPI, Request
import requests

app = FastAPI()

# 텔레그램 봇 정보 (본인의 값으로 수정하세요)
TELEGRAM_BOT_TOKEN = "8608136673:AAFp7PPRON868rhREFFvL_nKZ6WEuAfl8ug
"
CHAT_ID = "8839904195"

@app.post("/api/signup-notify")
async def signup_notify(request: Request):
    data = await request.json()
    
    # 텔레그램으로 보낼 메시지 구성
    user_email = data.get("record", {}).get("email", "알 수 없음")
    message = f"새로운 회원가입 알림! 이메일: {user_email}"
    
    # 텔레그램 API 호출
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)
    
    return {"status": "ok"}