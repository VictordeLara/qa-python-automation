from funcoes import *


def test_email_valido():
    assert email_valido("exemplo@gmail.com") is True
    assert email_valido("exemplo.com") is False

def test_dividir():
    assert divdir(4,2) == 2
    assert divdir(4,0) is None