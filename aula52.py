'''
enumerate
'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')