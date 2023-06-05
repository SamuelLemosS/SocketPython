import socket
import threading

HOST = 'localhost'
PORT = 50007
topicos = {}
lock = threading.Lock()

def handle_connection(conn):
    while True:
        tipoCliente = conn.recv(1024).decode()
        if not tipoCliente:
            break
        
        if tipoCliente == "pub":
            while True:
                topico = conn.recv(1024).decode()
                if topico == "sair":
                    break

                if topico not in topicos:
                    topicos[topico] = ""
                print("Novo publisher conectado no tópico:", topico)

                mensagem = conn.recv(1024).decode()
                topicos[topico] = mensagem
                print("Nova mensagem do tópico", topico, ":", mensagem)
        
        elif tipoCliente == "sub":
            topico = conn.recv(1024).decode()
            if topico in topicos:
                ultimaMensagem = topicos[topico]
                conn.send(ultimaMensagem.encode())
            else:
                conn.send("Esse tópico não existe ou não possui mensagens".encode())
            print("Novo subscriber conectado ao tópico", topico)

    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(6)
        print("Servidor escutando em", HOST + ":" + str(PORT))

        while True:
            conn, addr = s.accept()
            print('Conectado em:', addr)

            client_thread = threading.Thread(target=handle_connection, args=(conn,))
            client_thread.start()

start_server()
