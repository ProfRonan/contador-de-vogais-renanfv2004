
def count_vowels(string:str) -> int:
   

    vogais = "aeiou"
    contador = 0
    for caractere in string:
        for vogal in vogais:
            if vogal == caractere.lower():
                contador += 1
    return contador

print(count_vowels("AbCdeFG"))
