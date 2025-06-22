from app import is_evenNumber, is_palindrome


def test_is_evenNumber():
    assert is_evenNumber(4) is True
    assert is_evenNumber(5) is False


def test_is_palindrome():
    assert is_palindrome("katak") is True
    assert is_palindrome("tunggu") is False
