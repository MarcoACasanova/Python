# PROBLEMA 2 => Escreva um código que faça o FATORIAL de 20
# O fatorial de um número é o produto dele pelos seus antecessores maiores que 0
'''Exemplo:
0! = 1
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 * 1 = 6'''

fato = int(input('Digite o número: '))

def factorial(fato):
    fatorial = 1
    for i in range(1, fato):
        fatorial *= (fato + 1) - i
    if fatorial < 1:
        fatorial = 1
    return fatorial

print(factorial(fato))