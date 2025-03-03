from .pushover import send_message
import sys


def error_notification(exc_type, exc_value, exc_traceback):
    send_message("Error: " + str(exc_value))
    print(str(exc_value))


sys.excepthook = error_notification
