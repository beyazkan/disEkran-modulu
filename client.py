import socket
sunucuyaGonderilecekMesaj = "Aslı Dündar*Polat Alemdar*1*Uzm. Dt Aslı Dündar"
istemciSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = "127.0.0.1" 
port = 6000 
Buffer_Boyutu = 1024
istemciSoketi.connect((host, port)) 
print("Gonderilecek veri: ", sunucuyaGonderilecekMesaj)
istemciSoketi.send(sunucuyaGonderilecekMesaj.encode())
print ("Veri sunucuya basarili bir sekilde gonderildi.")
#sunucudanGelenMesaj = istemciSoketi.recv(Buffer_Boyutu)
#print ("Sunucudan Gelen Mesaj: ", sunucudanGelenMesaj)

print ("Sunucudan onay mesaji da alindigina gore; istemci tarafinda da baglanti koparilabilir")
#istemciSoketi.close()

# Sonuc