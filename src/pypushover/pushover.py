import os
import requests
from .keys import pushover_keys

api_key, user_key = pushover_keys()


def send_message(message: str, title: str | None = None):
    if not title:
        title = "Python"

    global api_key
    global user_key

    try:
        # URL for the Pushover API
        url = "https://api.pushover.net/1/messages.json"

        data = {
            "token": api_key,
            "user": user_key,
            "device": "iphone",  # might be different 4u
            "title": title,
            "message": message,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        requests.post(url, data=data, headers=headers)
    except Exception as e:
        print(f"An error occurred with notification: {e}")


if __name__ == "__main__":
    send_message("Hello from pypushover!")
