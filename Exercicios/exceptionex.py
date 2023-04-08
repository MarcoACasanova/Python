'''
aceitar três argumentos: um prompt, um limite inferior aceitável e um limite superior aceitável;
se o utilizador inserir uma string que não é um valor inteiro, a função deve emitir a mensagem Error: wrong input, e pedir ao utilizador para inserir o valor novamente;
se o utilizador introduzir um número que fica fora do intervalo especificado, a função deve emitir a mensagem Error: the value is not within permitted range (min..max) e pedir ao utilizador para inserir o valor novamente;
se o valor de input for válido, devolve-o como um resultado.
'''

def read_int(prompt, min, max):
    while True:
        try:
            valor = int(input(prompt))
            if valor < min or valor > max:
                raise ValueError("Error: the value is not within permitted range -10 to 10")
            return valor
        except ValueError:
            print('Wrong input, digite um número válido')
        

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)