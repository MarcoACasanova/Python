"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = "Ola Mundo"
print(variavel[-4])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[::-1]) # aqui pegou o inicio 0 o final 9 e escreveu de trás para frente
print(len(variavel))
