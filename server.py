import socket
import threading
import pickle

class GameServer:
    def __init__(self, host='localhost', port=5555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4)
        self.clients = []

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                self.broadcast(message, client_socket)
            except:
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                client.send(message)

    def run(self):
        print("Server started")
        while True:
            client_socket, addr = self.server.accept()
            print(f"Connection from {addr}")
            self.clients.append(client_socket)
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = GameServer()
    server.run()
