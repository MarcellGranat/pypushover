from pushover import send_message
from time import now

last_time = now()

def notify_after_elapsed_time(message: str, title: str | None = None, elapsed_time: int = 60) -> None:
    global last_time
    current_time = now()
    elapsed_time = current_time - last_time
    if elapsed_time > 60:
        send_message(message=message, title=title)
        last_time = current_time