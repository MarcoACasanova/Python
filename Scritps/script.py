import socket

# Define o IP alvo e as portas que serão verificadas
ip_alvo = input('Digite o IP a ser verificado ')
portas = [80, 443, 8080, 3306]

# Loop pelas portas e tenta se conectar a cada uma
for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10) # Define o tempo máximo de espera para conexão em 1 segundo
    resultado = sock.connect_ex((ip_alvo, porta))
    
    # Verifica se a porta está aberta
    if resultado == 0:
        print(f'A porta {porta} está aberta')
    else:
        print(f'A porta {porta} está fechada')
        
    sock.close()
