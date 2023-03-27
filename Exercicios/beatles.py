beatles = []
print("Step 1:", beatles)

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 2:", beatles)

for i in range(2):
    new_member = input('Insira os novos membros: ')
    beatles.append(new_member)
print("Step 3:", beatles)

del beatles[3]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(3, 'Ring Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))