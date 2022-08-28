from seasons import get_dob
import pytest
from datetime import date

def test_invalid_dob():
        with pytest.raises(ValueError):
            get_dob("January 1, 1999")

def test_correct():
    assert get_dob("2021-08-22") == "2021-08-22"