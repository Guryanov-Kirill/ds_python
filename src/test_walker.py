import pytest
from walker import Walker
import random

def test_get_random():
    data = [("A", 0.5), ("B", 0.5)]
    walker = Walker(data)
    result = walker.get_random()
    assert result in ["A", "B"]
