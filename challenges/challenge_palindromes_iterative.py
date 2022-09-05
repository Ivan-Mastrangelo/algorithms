def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False

    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
