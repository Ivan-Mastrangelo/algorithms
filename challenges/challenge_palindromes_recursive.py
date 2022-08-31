def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if not word or len(word) <= 2 and word[low_index] != word[high_index]:
        return False
    elif word[low_index] == word[high_index] and len(word) <= 2:
        return True
    word = word[1:high_index]
    high_index = len(word) - 1
    return is_palindrome_recursive(
        word, low_index, high_index)
