secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = 0

while number != secret_number:
    number = int(input('Digite o número secreto: '))
    if number != secret_number:
        print("Ha ha! You're stuck in my loop")
        continue
    else:
        print("Well done, muggle! You are free now")
        break
