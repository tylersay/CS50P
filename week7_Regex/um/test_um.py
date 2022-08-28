from um import count

def test_correct():
    assert count("um") == 1

def test_punctuation_around():
    assert count("um?") == 1

def test_inside_a_word():
    assert count("Um, thanks for the album.") == 1

def test_cap_and_elipsis():
    assert count("Um, thanks, um...") == 2