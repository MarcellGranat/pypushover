import os
import requests

try:
    api_key = os.environ['PUSHOVER_API_KEY']
    user_key = os.environ['PUSHOVER_USER_KEY']
except KeyError:
    raise Exception('PUSHOVER_API_KEY and PUSHOVER_USER_KEY must be set in the environment')

def send_message(message: str, title: str | None = None):
    if not title:
        title = "Python"
    
    try:
        # URL for the Pushover API
        url = "https://api.pushover.net/1/messages.json"

        data = {
            "token": api_key,
            "user": user_key,
            "device": "iphone", # might be different 4u
            "title": title,
            "message": message
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        requests.post(url, data=data, headers=headers)
    except Exception as e:
        print(f"An error occurred with notification: {e}")

if __name__ == "__main__":
    send_message("Hello from pypushover!")
