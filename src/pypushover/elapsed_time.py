from .pushover import send_message
from time import time

last_time = time()
sent_first_message = False

def notify_after_elapsed_time(message: str, title: str | None = None, elapsed_time: int = 60, init = True) -> None:
    global last_time
    global sent_first_message
    current_time = time()
    elapsed_time = current_time - last_time

    if not sent_first_message and init:
        send_message(message=message, title=title)
        sent_first_message = True
        last_time = current_time
        return

    if elapsed_time > elapsed_time:
        send_message(message=message, title=title)
        last_time = current_time

if __name__ == "__main__":
    notify_after_elapsed_time("Hello from pypushover!")