import pytest
import os
from pypushover.keys import dot_path_finder

def test_dot_path_finder():
    assert dot_path_finder() == os.getcwd() + "/.env"