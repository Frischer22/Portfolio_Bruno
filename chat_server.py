import socket
import threading

host = "192.168.0.2"
port = 32012

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nomes = []

def chat(message):
    for client in clients:
        client.send(message)


def verify(client):
    while True:
        try:
            message = client.recv(2048)
            chat(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nome = nomes[index]
            chat(f'{nome} deixou o chat!' .encode('utf-8'))
            nomes.remove(nome)
            break

def recebe():
    while True:
        client, address = server.accept()
        print(f"Conexão do IP {str(address)}")
        client.send('NICK' .encode('utf-8'))
        nome = client.recv(2048).decode('utf-8')
        nomes.append(nome)
        clients.append(client)

        print(f'Nome do cliente é {nome}!')
        chat(f'{nome} se juntou ao chat!'.encode('utf-8'))
        client.send('Conectou ao chat!'.encode('utf-8'))

        thread = threading.Thread(target=verify, args=(client,))
        thread.start()

print("Chat está ativo")
recebe()
