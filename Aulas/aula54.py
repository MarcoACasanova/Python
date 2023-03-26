'''
Split e join com list e str
split divide uma string
join une uma string
'''

frase = "Olha só que, coisa interessante"
lista_frases = frase.split(',') # eu solicitei ao split que separasse pela virgula, vide exemplo rodando o algoritmo
print(lista_frases)
# repare que ficou 'Olha só que' , 'Coisa interessante'
lista_palavras = frase.split() # aqui não dei nenhum tipo de informação então ele fará em modo "automático"
# vide o exemplo que ele separou tudo, acho que agora está mais claro como funciona
print(lista_palavras)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) # o strip 'corta' os espaços das frases
# lstrip corta espaços da esquerda e rstrip direita

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip() #alterando a lista
print(lista_frases)

'''
Join
'''
frases_unidas = ' - '.join(lista_frases) # o primeiro str é o que vc quer que une
print(frases_unidas)