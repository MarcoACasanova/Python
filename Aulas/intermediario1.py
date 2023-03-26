'''
Introdução a funções em python
Funções são trechos do código usados para
replicar determinada ação ao longo do seu código
por padrão, funções python retornam None
'''
'''def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 'C')
imprimir('A', 2, 3) # eu posso chamar a função com códigos diferentes
'''
def saudacao(nome = 'sem nome'):
    print(f'Olá, {nome}!')
saudacao('Luiz Otávio')
saudacao('Marco')
saudacao() # se eu passar um valor ele irá usar,
#se eu não passar um valor ele irá usar o pré-definido