a = 'AAA'
b = 'BB'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)
# parametro \/
str = 'a={nome1} b={nome2} c={nome3}'
formatoo = str.format(nome1=a, nome2=b, nome3=c)
print(formatoo)