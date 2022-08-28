from fuel import convert, gauge
import pytest

# def main():
#     test_correct_threequarters()



# 3/4 shld output 75%
# 1/4 OUTPUT 25%
def test_correct_threequarters():
    assert convert("3/4") == 75
    assert gauge(75) == "75%"



def test_correct_onequarter():
    assert gauge(convert("1/4")) == "25%"



# # 4/4 output F
def test_full():
    assert gauge(convert("4/4")) == "F"
    assert gauge(convert("99/100")) == "F"

# # # 0/4 output E
def test_empty():
    assert gauge(convert("0/4")) == "E"
    assert gauge(convert("1/100")) == "E"


# # 4/0 prompt ZeroDivisionError
def test_zeroError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

# #three/four valueError
# # 1.5/3 raise ValueError
def test_valueError():
    with pytest.raises(ValueError):
        convert("three/four")

    # with pytest.raises(ValueError):
    #     convert("1.5/3")





#     monkeypatch.setattr('builtins.input', lambda _: "1.5/3")
#     frac = input("Fraction: ")
#     assert convert(frac) == ValueError


# if __name__ == "__main__":
#     main()