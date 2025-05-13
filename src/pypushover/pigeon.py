import time
from typing import Callable

from pydantic import BaseModel

from .pushover import send_message


class Pigeon(BaseModel):
    """
    A class representing a waiter that acts only when the wait time is reached.

    Attributes:
        wait_time (int): The time to wait before sending the notification.
        max_wait_time (int): The maximum time to wait before sending the notification.
        func (Callable): The function to call when the wait time is reached.
    """

    wait_time: int | float = 0
    last_time: float = time.time()
    func: Callable = send_message

    def __call__(self, *args, **kwargs):
        """
        Call the function if the wait time is reached.
        """
        current_time = time.time()
        elapsed_time = current_time - self.last_time

        if elapsed_time >= self.wait_time:
            self.func(*args, **kwargs)
            self.last_time = current_time

if __name__ == "__main__":
    pigeon = Pigeon(
        wait_time=5,
        func=lambda: print("Hello from pypushover!"),
    )

    for i in range(11): # expected to print 2 times
        time.sleep(1)
        pigeon()

