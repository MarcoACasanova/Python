lista = [10, 20, 30, 40]
lista.append('Marco')
print(lista)
nome = lista.pop()
print(lista, nome)
lista.append(1234)
print(lista)
del lista[-1]
print(lista)
# comando lista.clear() (limpa a lista inteira)
lista.insert(0, 5) # aqui recebemos dois argumentos, o primeiro argumento no exemplo "0" é a posição da lista o segundo argumento
# no caso "5" é o valor que você irá colocar, lembrando que não necessariamente deverá ser um int, pode ser Str ou float
print(lista)
lista.insert(0, 0.5) # aqui adicionamos um float.
print(lista)
print(lista[5]) # aqui pegamos um posição existente
# print(lista[6]) # aqui criamos um erro, até pq ainda não existe a posição 6 na lista
# comentamos o item acima para não causar um break no algoritmo
