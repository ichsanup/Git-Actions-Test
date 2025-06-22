# app.py
def is_evenNumber(x):
    return x % 2 == 0


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]
