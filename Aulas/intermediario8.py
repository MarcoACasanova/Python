def calculo(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplicação = calculo(10,2,3,4,5)
print(multiplicação)

def par_impar():
    numero = int(input('digite o seu número: '))
    if numero % 2 == 0:
       print('Este número é par')
    else:
        print('esse número é impar')

par_impar()