hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hat_list[2] = int(input('Digite um novo número no meio da lista: '))

del(hat_list[4])

print(len(hat_list))

print(hat_list)
