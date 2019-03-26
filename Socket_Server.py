import socket
from threading import *
import config as conf
import sound

class Socket_Server(Thread):
    done = False
    paket = ""
    dizi = []
    hasta = []

    def __init__(self):
        Thread.__init__(self)
        print("Socket Server Sınıfı Yüklendi.")

    def run(self):
        while not self.done:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind((conf.Host, conf.Port))
                sock.listen()
                print("Bağlantı Bekleniyor.")
                connect, address = sock.accept()
                with connect:
                    print("Bağlanan Adres: ", address)
                    while True:
                        data = connect.recv(1024)
                        self.paket = data.decode('utf-8')
                        self.dizi = str(self.paket).split("*")
                        sound_vari = sound.Sound(self.dizi[1])
                        self.hasta.append(self.get_dizi())
                        break;

    def stop(self):
        pass
        
    def get_dizi(self):
        return [self.dizi[0].strip(), self.dizi[1], self.dizi[2], self.dizi[3]]

    def get_hasta(self):
        return self.hasta

    


