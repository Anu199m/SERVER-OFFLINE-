import requests
import time

print("🔁 FB Auto Messenger Bot Running...")

access_token = input("🔑 Enter your FB Page Token:\n> ")
convo_id = input("🆔 Enter Conversation ID:\n> ")
message = input("💬 Enter your message:\n> ")
interval = int(input("⏱ Interval in minutes:\n> "))

def send_msg():
    url = f"https://graph.facebook.com/v18.0/{convo_id}/messages"
    payload = {
        "message": {"text": message},
        "access_token": access_token
    }
    r = requests.post(url, json=payload)
    print("✅ Message sent:", r.json())

while True:
    send_msg()
    time.sleep(interval * 60)
