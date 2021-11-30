# Laboratório 1 - Marcos Paulo Moraes

import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() 

# conecta-se com o par passivo
sock.connect((HOST, PORTA)) 

mensagem = input("Envie uma mensagem (para parar, envie STOP): ")

while (mensagem != "STOP"):

    # envia uma mensagem para o par conectado
    sock.send(bytes(mensagem,'UTF-8'))

    #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
    msg = sock.recv(1024) # argumento indica a qtde maxima de bytes da mensagem

    # imprime a mensagem recebida
    print(str(msg,  encoding='utf-8'))
    
    mensagem = input("Envie uma mensagem (para parar, envie STOP): ")

# encerra a conexao
sock.close() 
