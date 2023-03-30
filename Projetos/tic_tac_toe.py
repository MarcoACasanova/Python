def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|    {}  |   {}   |  {}    |".format(board[0], board[1], board[2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|    {}  |   {}   |  {}    |".format(board[3], board[4], board[5]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|    {}  |   {}   |   {}   |".format(board[6], board[7], board[8]))
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
# A função aceita o status atual do tabuleiro, pede a jogada do usuário,
    # verifica a entrada e atualiza o tabuleiro de acordo com a escolha do usuário.
    while True:
        user_move = input("Digite a posição para jogar (1-9): ")
        if user_move.isdigit() and int(user_move) in range(1, 10) and board[int(user_move) - 1] == ' ':
            board[int(user_move) - 1] = 'O'
            break
        else:
            print("Entrada inválida. Por favor, digite um número entre 1 e 9 que corresponda a uma posição vazia no tabuleiro.")
            

def make_list_of_free_fields(board):
    # A função percorre o tabuleiro e constrói uma lista com todos os quadrados vazios;
    # a lista é composta de tuplas, onde cada tupla é um par de números de linha e coluna.
    free_fields = []
    for i in range(9):
        if board[i] == ' ':
            free_fields.append((i // 3, i % 3))
    return free_fields


def victory_for(board, sign):
    # A função analisa o status do tabuleiro para verificar se
    # o jogador que usa 'O' ou 'X' ganhou o jogo
    win_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pos in win_pos:
        if all(board[i] == sign for i in pos):
            return True
    return False

import random

def draw_move(board):
    # A função desenha a jogada do computador e atualiza o tabuleiro.
    free_fields = make_list_of_free_fields(board)
    if (1, 1) in free_fields:
        computer_move = (1, 1)
    else:
        computer_move = random.choice(free_fields)
    board[computer_move[0] * 3 + computer_move[1]] = 'X'

board = [' '] * 9

draw_move(board)  # Máquina começa jogando
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Você venceu!")
        break
    elif victory_for(board, 'X'):
        print("O computador venceu!")
        break
    elif len(make_list_of_free_fields(board)) == 0:
        print("Empate!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Você venceu!")
        break
    elif victory_for(board, 'X'):
        print("O computador venceu!")
        break
    elif len(make_list_of_free_fields(board)) == 0:
        print("Empate!")
        break
