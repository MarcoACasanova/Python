x = [1,2,3,4,5,6,7,8,9]
fim = len(x) - 1
aux = 0

for i in range(len(x)//2):
    aux = x[i]
    x[i] = x[fim]
    x[fim] = aux
    fim -= 1

print(x)