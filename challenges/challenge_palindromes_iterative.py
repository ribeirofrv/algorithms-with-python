def is_palindrome_iterative(word):
    if not word:
        return False

    new_word = ""
    index = -1

    while len(word) != len(new_word):
        new_word += word[index]
        index -= 1

    return True if word == new_word else False
