def soma_numeros_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(soma)
    


soma_numeros_pares([1,2,3,4,5,6])

