def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = (235.215/(liters/100)) / 100 # vide comentário no final do alg.
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1.609344
    liters_per_100km = 100 / (km_per_gallon / 3.785411784)
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


'''
Comentário sobre a formula, para chegar nela observei a formula que o google fazia para converter o que era solicitado, já que não sou matemático ^^
Como pelo exercicio os outputs já nos era fornecidos, eu fiz a pequena modificação de incrementar mais uma divisão por 100.
a primeira parte sem dividir por 100 no final dava o valor de saída de 6031 e o output solicitado era 60.31...
'''