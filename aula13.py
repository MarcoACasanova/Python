nome = 'Marco Antonio Casanova'
altura = 1.69
peso = 87.1
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
print(linha_1)
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'
print(linha_2)
print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)

# breve introdução f-strings