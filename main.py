from fastapi import FastAPI
import requests

app = FastAPI()

# 아래 부분이 바로 /send 주소를 만들어주는 코드입니다!
@app.get("/send")
def send_telegram_message():
    token = "8608136673:AAFp7PPRON868rhREFFvL_nKZ6WEuAfl8ug"
    chat_id = "8839904195"
    message = "테스트 메시지입니다!"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    return {"message": "메시지 전송 성공!"}

# 텔레그램 봇 정보 (본인의 값으로 수정하세요)
TELEGRAM_BOT_TOKEN = "8608136673:AAFp7PPRON868rhREFFvL_nKZ6WEuAfl8ug"
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