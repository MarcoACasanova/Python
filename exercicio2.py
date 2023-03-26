import os

secreta = 'perfume'
letras_acertadas = " "
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == secreta:
        os.system('cls')
        print('Você ganhou parabéns.')
        print('A palavra era', palavra_formada)
        print('Tentativas:', tentativas)
        letras_acertadas = " "
        tentativas = 0