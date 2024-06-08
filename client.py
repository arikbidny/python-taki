import socket
import threading
import pickle
from encryption import encrypt_message, decrypt_message

class GameClient:
    def __init__(self, host='localhost', port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send(self, message):
        encrypted_message = encrypt_message(message)
        self.client.send(encrypted_message)

    def receive(self):
        while True:
            try:
                encrypted_message = self.client.recv(1024)
                message = decrypt_message(encrypted_message)
                print(f"Received: {message}")
            except:
                print("An error occurred")
                self.client.close()
                break

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        while True:
            message = input()
            self.send(message)

if __name__ == "__main__":
    client = GameClient()
    client.run()
