string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, c = lista
print(a, c)

for nome in lista:
    print(nome, end=' ')
print()
print(*lista)
print(*string)
print(*tupla)