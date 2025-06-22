from App import is_evenNumber, is_palindrome
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_is_evenNumber():
    assert is_evenNumber(4) == True
    assert is_evenNumber(5) == False


def test_is_palindrome():
    assert is_palindrome("katak") == True
    assert is_palindrome("tunggu") == False
