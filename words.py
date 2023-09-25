def print_upper_words(words, starting_letters):
    """Takes in list of words and prints each word in upper case."""
    [print(word.upper()) for word in words if word[0].upper() in [letter.upper() for letter in starting_letters]]