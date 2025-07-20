import os
import time
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_report():
    text = "📊 گزارش تستی مهرام: همه‌چی مرتبه!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

while True:
    send_report()
    time.sleep(900)  # هر ۱۵ دقیقه
