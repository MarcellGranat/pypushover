from pypushover import send_message
import sys

def error_notification(exc_type, exc_value, exc_traceback):
  send_message("Error: " + str(exc_value))
  print(exc_traceback)

sys.excepthook = error_notification