import socket
import config as conf
import sound

class Socket_Server():
    done = False
    paket = ""
    dizi = []

    def __init__(self):
        print("Socket Server Sınıfı Yüklendi.")

    def start(self):
        while not done:
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
                        self.dizi = str(stringifade).split("*")
                        sound_vari = sound.Sound(dizi[1])
                        break;

    def stop(self):
        pass
        
    def get_dizi(self):
        return [dizi[0].strip(), dizi[1], dizi[2], dizi[3]]

    


