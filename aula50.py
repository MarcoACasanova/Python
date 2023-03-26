'''
Introdução ao desempacotamento + tuples (tuplas)
'''
# *resto é necessário o '*' para que "compact" todos os valores que sobraram. 
_, nome2, *_ = ['Maria', 'Susana', 'Marco']
# se observarmos acima temos 2 variáveis para 3 valores, isso geraria um erro, onde nós "arrumamos" com a primeira explicação
print(nome2, _) # convenção usada em python o underline é para indicar que não usaremos a variável
