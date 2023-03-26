numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_conversao = int(numero)
    if numero_conversao % 2 == 0:
        print('Este número é Par')
    else:
        print('Este número é impar')
else:
    print('Você não digitou um número inteiro')


# exercicio acima corrigido com o prof.

hora = input('Qual é a hora: ')
hora_conversao = int(hora)

if hora_conversao >= 0 and hora_conversao < 12:
    print('Bom dia!')
elif hora_conversao >= 12 and hora_conversao < 18:
    print('Boa tarde')
else:
    print('Boa noite')

# exercicio realizado e é super fácil o de cima, porém, tem que ver como faria para colocar hora exata por exemplo com ':'

nome = input('Escreve seu nome, somente seu nome: ')

if len(nome) <= 4:
    print('Seu nome é pequeno')
elif len(nome) > 4 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é extenso')