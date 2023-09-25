def same_frequency(num1, num2):
    """
    Takes in two numbers, num1 and num2. Returns true if they have the
    same frequency of digits, false otherwise.
    """
    num1_freqs = count_frequencies(str(num1))
    num2_freqs = count_frequencies(str(num2))

    return num1_freqs == num2_freqs

def count_frequencies(input):
    """
    Takes an iterable as input and returns the frequency of each item
    in the input in a dict.
    """
    freqs = {}
    for item in input:
        freqs[item] = ((item in freqs and freqs[item]) or 0) + 1
    return freqs