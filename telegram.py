import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    r = requests.post(url, data=payload)
    print(r.text)
    return r.status_code == 200


def send_photo(photo_path, caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with open(photo_path, "rb") as photo:
        files = {
            "photo": photo
        }

        data = {
            "chat_id": CHAT_ID,
            "caption": caption,
            "parse_mode": "HTML"
        }

        r = requests.post(url, files=files, data=data)

    print(r.text)
    return r.status_code == 200
