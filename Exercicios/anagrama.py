def anagrama(frase_um, frase_dois):
    frase_um = frase_um.replace(" ", "").lower()
    frase_dois = frase_dois.replace(" ", "").lower()

    if len(frase_um) != len(frase_dois):
        return False

    return sorted(frase_um) == sorted(frase_dois)

frase_um = input("Escreva a primeira frase: ")
frase_dois = input("Escreva a segunda frase: ")

if anagrama(frase_um, frase_dois):
    print("As frases são anagramas.")
else:
    print("As frases não são anagramas.")
