'''
While
executa uma ação enquanto uma condição for verdadeira
'''

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('teste')
        continue

    print(contador)

    if contador == 40 :
        break

print('Acabou')