import random

def gera_cpf():
    # Gera os 9 primeiros dígitos aleatoriamente
    cpf = [random.randint(0, 9) for i in range(9)]

    # Calcula o primeiro dígito verificador
    soma = sum([cpf[i] * (10-i) for i in range(9)])
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    cpf.append(resto)

    # Calcula o segundo dígito verificador
    soma = sum([cpf[i] * (11-i) for i in range(10)])
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    cpf.append(resto)

    # Retorna o CPF como string
    return ''.join(map(str, cpf))

# Exemplo de uso:
cpf_gerado = gera_cpf()
print("CPF gerado:", cpf_gerado)
