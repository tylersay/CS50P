import pytest
from calculator import square

########################
# Using PYTEST
########################
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-3) == 9
    assert square(-2) == 4


def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

########################
# conventional testing
########################
# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 sq not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 sq not 9")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("neg3 sq not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 sq not 0")


# if __name__ == "__main__":
#     main()