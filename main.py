"""This program counts the number of vowels in a string."""
def count_vowels(string:str) -> int:
    """
    Takes in a string and returns the number of vowels in the string.
    Args:
        string (str): The string to count vowels in.
    Returns:
        int: The number of vowels in the string.
    """

    vogais = "aeiou"
    contador = 0
    for caractere in string:
        for vogal in vogais:
            if vogal == caractere.lower():
                contador += 1
    return contador

print(count_vowels("AbCdeFG"))
