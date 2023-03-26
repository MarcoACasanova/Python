'''
Iterando strings com while
'''
#       012345678910   
nome = "Marco Antonio Casanova" #iteráveis # 22 caracteres

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)