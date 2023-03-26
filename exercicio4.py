'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com erros de indices
inexistentes na lista.
'''
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar')

    if opcao == 'i':
        os.system('cls')
        valor = input("valor: ")
        lista.append(valor)
    elif opcao == 'a':
        indice_str=input(
            'Escolha o indice para apagar'
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolhe i, a ou l')