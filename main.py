main.py 
import os
from flask import Flask, request
import requests

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.get(URL + f"sendMessage?chat_id={chat_id}&text={text}")

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.get_json()

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            send_message(chat_id, "Bot ishlayapti! Siz yozgan matn: " + text)

        return {"ok": True}

    return "Bot ishlayapti!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
