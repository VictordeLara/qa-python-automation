def is_possitive(numero):
    return numero > 0


def test_eh_possitivo():
    assert is_possitive(4) is True
    assert is_possitive(-5) is False