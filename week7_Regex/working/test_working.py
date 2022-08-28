from working import convert
import pytest

#value error

def test_dash():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")



def test_60min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_no_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_with_min():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
