# interpolação básica de strings
# s - strings
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Marco'
preco = 1000.9876543
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))
