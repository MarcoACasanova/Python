password = 'chupacabra'
word = ''

while word != password:
    word = input('Digite a senha secreta: ')
    if word == password:
        print("You've successfully left the loop")
        break
    else:
        print('Wrong password')
        continue