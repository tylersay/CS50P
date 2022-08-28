from plates import is_valid

def test_GME240():
    assert is_valid("GME420") == True
    assert is_valid("RC") == True
    assert is_valid("A") == False
    assert is_valid("GMETOTHEMOON") == False

def test_firsttwo():
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("AA") == True

def test_numplacement():
    assert is_valid("GME420") == True
    assert is_valid("A123F") == False
    assert is_valid("123GME") == False
    assert is_valid("12") == False


def test_firstnumiszero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False

def test_alnum():
    assert is_valid("-abc-") == False
    assert is_valid("P3.14") == False
    assert is_valid("GME 24") == False

def test_startnum():
    assert is_valid("420GME") == False


