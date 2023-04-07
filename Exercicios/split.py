def mysplit(strng):
    words = [] # criação da lista vazia
    word = "" # criação da varíavel para exclusão dos espaços e adicionar as palavras a lista.

    for char in strng: # loop for para fazer a verificação e destinação das substrings
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word: # esse if final é para o caso da ultima substring não ter sido adicionada a lista.
        words.append(word)

    return words    

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))