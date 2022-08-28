from twttr import shorten

def test_shorten():
    assert shorten("Hello, my name is Tyler") == "Hll, my nm s Tylr"

def test_numbers():
    assert shorten("123 hello hello") == "123 hll hll"

def test_cap():
    assert shorten("All Your Base Are Belong To Us") == "ll Yr Bs r Blng T s"