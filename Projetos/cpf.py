'''
CPF: 746.824.890-70
COLETE A SOMA DOS 9 PRIMEIROS DIGITOS DO CPF
MULTIPLICANDO CADA UM DOS VALORES POR UMA
CONTAGEM REGRESSIVA COMAÇANDO DE 10

EX.: 746.824.890-70
    10  9  8  7  6  5  4  3  2
     7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27  0

SOMAR TODOS OS RESULTADOS:
70+36+48+56+12+20+32+27+0 = 301
MULTIPLICAR O RESULTADO ANTERIOR POR 10
301 * 10 = 3010
OBTER O RESTO DA DIVISÃO DA CONTA ANTERIOR POR 11
3010 % 11 = 7
SE O RESULTADO ANTERIOR FOR MAIOR QUE 9
    RESULTADO É 0
CONTRÁRIO DISSO:
    O RESULTADO É O VALOR DA CONTA

O primeiro digito do cpf é 7
'''
def valida_cpf(cpf):
    """
    Valida um CPF.
    """
    cpf = str(cpf)
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    # Calcula o primeiro dígito verificador.
    soma = 0
    for i in range(0, 9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[9]):
        return False
    # Calcula o segundo dígito verificador.
    soma = 0
    for i in range(0, 10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True

cpf = input('Digite seu cpf: ')
if valida_cpf(cpf):
    print('CPF válido')
else:
    print('CPF Inválido')
