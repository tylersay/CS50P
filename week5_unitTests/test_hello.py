from hello import hello

def test_default():
    assert hello() == "hello, world"


def test_arguemnt():
    assert hello("David") == "hello, David"
