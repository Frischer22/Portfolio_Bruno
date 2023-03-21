import socket
import threading

nome = input("Insira seu nome: ")

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('192.168.0.2', 32012))

def recebe():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nome.encode('utf-8'))
            else:
                print(message)
        except:
            print("A mensagem nÃ£o pode ser enviada, ocorreu um erro!")
            client.close()
            break

def escreve():
    while True:
        messagem_log = f'{nome}: {input("")}'
        client.send(messagem_log.encode('utf-8'))
    

receive_thread = threading.Thread(target=recebe)
receive_thread.start()

write_thread = threading.Thread(target=escreve)
write_thread.start()
