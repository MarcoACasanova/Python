"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Marco Antonio'
outra_string = f'{string[:3]}ABC{string[4:]}'
print(string[3])
print(outra_string)
print(string.zfill(10))