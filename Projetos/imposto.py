income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = max(0, tax)
tax = round(tax)

print("The tax is:", tax, "thalers")

# esse exercicio em particular sem o tax = max(0, tax) toda vez que retornava valor abaixo dos 85 mil ele calculava errado.