# PROBLEMA 3 => Verifique qual item do array é um PALINDROMO ["Saíram o tio e oito Marias", "O lobo ainda ama o bolo", "Seco de raiva, coloco no colo caviar e doces"]

array = ['sairam o tio e oito marias', 'o lobo ainda ama o bolo', 'seco de raiva coloco no colo caviar e doces']

def palindromo():
    for i in range(len(array)):
        txt = str(array[i])
        print(txt)
        if txt.replace(" ", "")[::-1] == txt.replace(" ", ''):
            print('É Palindromo.')
        else:
            print('Não é palindromo')
palindromo()