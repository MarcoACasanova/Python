# soma de números pares

n = int(input('Digite quantos números serão inseridos.'))
insert = 0
lista = []

for i in range(n):
    insert = int(input('Insira o número: '))
    lista.append(insert)

soma = 0

for num in range(len(lista)):
    if lista[num] % 2 == 0:
        soma += lista[num]

print(lista)
print(soma)