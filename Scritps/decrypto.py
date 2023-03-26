from cryptography.fernet import Fernet
import os
from pathlib import Path

pasta = Path ('D:\Arquivos')
ext = ('.txt')

def decrypto():
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(ext):
            caminho = pasta / arquivo

            a = open(caminho, 'rb')
            dados_cripto = a.read()
            a.close()

            chave = 'H2eP02mu18qdHk-Fl3587-TL1OnZlsviNNMl4LMxHks='

            k = Fernet(chave)
            dados = k.decrypt(dados_cripto)

            file = open(caminho, 'wb')
            file.write(dados)
            file.close()

decrypto()