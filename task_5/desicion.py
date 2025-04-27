text = 'aBbA'


def is_palindrome(text):
    return text.lower() == text.lower()[::-1]


print(is_palindrome(text))
