birthday = str(input("Digite aqui sua data de nascimento: "))
soma = 0
day_life = 0 

for i in range(len(birthday)):
    soma += int(birthday[i])
soma = str(soma)

for i in range(len(soma)):
    day_life += int(soma[i])

print(day_life)