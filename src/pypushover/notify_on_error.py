from pypushover import pushover_notification
import sys

def error_notification(exc_type, exc_value, exc_traceback):
  pushover_notification("Error: " + str(exc_value))
  print(exc_traceback)

sys.excepthook = error_notification