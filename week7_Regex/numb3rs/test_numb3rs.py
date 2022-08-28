from numb3rs import validate

def test_correct():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True

def test_over255():
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False

def test_words():
    assert validate(r"cat") == False

def test_format():
    assert validate(r"1") == False
    assert validate(r"1.2") == False
    assert validate(r"1.2.3") == False