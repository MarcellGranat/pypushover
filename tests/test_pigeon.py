from time import sleep

from pypushover import Pigeon


def test_pigeon():
    """
    Test the Pigeon class.
    """


    x = 0

    def increment():
        nonlocal x
        x += 1

    pigeon = Pigeon(
        wait_time=5,
        func=increment,
    )

    # Call the pigeon function 11 times
    for i in range(11):
        sleep(1)
        pigeon()

    assert x == 2, "Pigeon should have called the function twice" 