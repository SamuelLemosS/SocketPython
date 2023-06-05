import socket
import time

HOST = "localhost"
PORT = 50007
tipoCliente = input("Você deseja publicar? (Caso não, será um assinante)")

if tipoCliente.lower() == "sim" or tipoCliente.lower() == "s":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send("pub".encode())

        while True:
            topico = input("Digite o tópico que deseja enviar (ou 'sair' para encerrar):\n")
            if topico.lower() == "sair":
                break
            s.send(topico.encode())

            mensagem = input("Digite a mensagem que deseja enviar:\n")
            s.send(mensagem.encode())

        s.send("sair".encode())  

elif tipoCliente.lower() == "nao" or tipoCliente.lower() == "n" or tipoCliente.lower() == "não":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send("sub".encode())

        topico = input("Digite o tópico que deseja receber:\n")
        s.send(topico.encode())

        while True:
            ultimaMensagem = s.recv(1024).decode() #ele nao pega nada quando passa pela segunda vez
            if ultimaMensagem:
                print("A última mensagem do topico",topico,"é: ",ultimaMensagem)
                ultima = ultimaMensagem
            else:
                print("Nenhuma nova mensagem")

            time.sleep(1)

else:
    print("Digite 'sim' ou 'não', por favor.")
