palavra_um = ''
palavra_dois = ''

def verificar_letras(palavra_um, palavra_dois):
    for letra in palavra_um:
        if letra not in palavra_dois:
            print('no')
    
    


palavra_um = input("Digite aqui a palavra desejada: ")
palavra_dois = "Nabucodonosor"

verificar_letras(palavra_um, palavra_dois)