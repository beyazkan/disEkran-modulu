import socket
import config as conf

class Socket_Client():
    def __init__(self, msj = "kapat"):
        self.msj = msj
        self.cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.cli_socket.connect((conf.Host, conf.Port))

    def send(self):
        print("Gonderilecek veri: ", self.msj)
        self.cli_socket.send(self.msj.encode())