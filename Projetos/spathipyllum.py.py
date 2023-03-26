name = '0'

while name != 'spathipyllum' or 'Spathipyllum':
    name = input('Escreva o nome da planta que purifica o ar: ')
    if name == 'spathipyllum':
        print('No, i want a big Spathiphyllum!')
        continue
    elif name == 'Spathipyllum':
        print('Yes - Spathiphyllum is the best plant ever!')
        break
    else:
        continue