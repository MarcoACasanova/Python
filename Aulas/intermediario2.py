'''
Argumentos nomeados e não nomeados em Python
Argumento posicional == não nomeados
'''
# Definição da função 
def soma(x, y, z):
    print(x + y)

# Agora vou executar a função
soma(1, 2, 1) # os que estão dentro do parenteses são argumentos
soma(y=2, x=1, z=1) # aqui são argumentos nomeados.
