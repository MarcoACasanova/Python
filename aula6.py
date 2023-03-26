# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1)
print('a' + 'b')
print(int("1"), type(int('1'))) # aqui fizermos a coerção dos dois dados, e no segundo exemplo pedimos para voltar o type 
print(int('1') + 1) # Neste exemplo fizemos a coerção do primeiro dado que estava em STR para INT
print(float('1')) # aqui aplicamos a coerção em STR > FLOAT
print(bool('1'))
print(bool('0')) # exemplo simples mostrando que é verdadeira
print(bool()) # exemplo simples que mostra um FALSE