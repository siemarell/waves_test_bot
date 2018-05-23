from config import BOT_URL
import requests
_s = requests.Session()


def send_message(chat_id, message):
    data = {
        "chat_id": chat_id,
        "text": message
    }
    resp = _s.post(f"{BOT_URL}sendMessage", json=data)
    return resp.status_code == 200
