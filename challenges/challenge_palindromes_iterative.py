def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    while len(word) >= 2:
        last_index = len(word) - 1
        if word[0] == word[last_index]:
            word = word[1:last_index]
        else:
            return False
    return True
