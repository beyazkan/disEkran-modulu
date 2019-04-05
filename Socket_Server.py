import socket
from threading import *
import config as conf
from threading import *
import queue

class Socket_Server(Thread):
    done = False
    paket = ""
    dizi = []
    hasta = []

    def __init__(self, q, q_done):
        Thread.__init__(self)
        self.q = q
        self.q_done = q_done
        print("Socket Server Sınıfı Yüklendi.")

    def run(self):
        while not self.done:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind(('', conf.Port))
                sock.listen()
                print("Bağlantı Bekleniyor.")
                connect, address = sock.accept()
                with connect:
                    print("Bağlanan Adres: ", address)
                    while True:
                        connect.send("Trtek Sunucusuna Bağladınız.".encode())
                        data = connect.recv(conf.Buffer_limit)
                        self.paket = data.decode('utf-8')
                        if self.paket == "kapat":
                            self.done = True
                            break
                        self.dizi = str(self.paket).split("*")
                        self.q.put(self.get_dizi())
                        break

    def stop(self):
        pass
        
    def get_dizi(self):
        return [self.dizi[0].strip(), self.dizi[1], self.dizi[2], self.dizi[3]]

    def get_hasta(self):
        return self.hasta

    


