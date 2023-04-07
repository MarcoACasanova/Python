def caesar_cipher(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

text = input("Digite o texto a ser criptografado: ")
while True:
    try:
        shift = int(input("Digite o valor de deslocamento (1 a 25): "))
        if shift < 1 or shift > 25:
            raise ValueError
        break
    except ValueError:
        print("Valor inválido. Tente novamente.")

print("Texto criptografado: ", caesar_cipher(text, shift))
