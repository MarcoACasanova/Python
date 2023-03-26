lista = ['Maria', 'Helena', 'Luiz']

lista.append('Joao')

indices = range(len(lista))
print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))