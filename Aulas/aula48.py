"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # o que está dentro do () será incluso na lista que vc solicitou no inicio do código
print(lista_c)
print(lista_a) # exemplo de extend

'''
Cuidados com dados mutáveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutável)
'''

lista = ['Luiz', 'Maria']
lista_b = lista.copy()
lista[0] = 'Qualquer coisa'
print (lista_b)
