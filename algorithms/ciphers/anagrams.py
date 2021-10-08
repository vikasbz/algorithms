def check_anagram(word_1: str, word_2: str):
    return sorted(word_1.strip().lower()) == sorted(word_2.strip().lower())


if __name__ == "__main__":
    is_anagram = check_anagram("sator", "rotas")
    print(is_anagram)
