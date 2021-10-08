def check_palindrome(word_1: str, word_2: str):
    return word_1.strip().lower() == word_2.strip().lower()[::-1]


if __name__ == "__main__":
    is_palindrome = check_palindrome("Ana", "ANA")
    print(is_palindrome)
