from bank import value

def test_cap_hello():
    assert value("Hello") == 0

def test_no_h():
    assert value("What's upp dawg") == 100

def test_hawt_dawg():
    assert value("hawt dawg") == 20