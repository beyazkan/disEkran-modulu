# Baslangic
 
import socket  
sunucuSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = '127.0.0.1'  
port = 6000
Buffer_Boyutu = 1024
sunucuSoketi.bind((host, port))
sunucuSoketi.listen(5)
print ("\n" + str(port), "portu acildi ve baglantilar dinleniyor" + "\n")
baglantiAdedi = 1
 
 
while True:
	print ("\n" + "*******************************************" + "\n")
	print (baglantiAdedi, "nolu baglanti bekleniyor....")
	baglanti, istemciIPAdresi = sunucuSoketi.accept() # Baglanti talebi olusturuldu
	print ("istemciden gelen", baglantiAdedi, "nolu baglanti kabul edildi")
	print ('Baglanan istemci IP Adresi ve Portu:', istemciIPAdresi)
	print ("Istemciden mesaj alinmasi bekleniyor...")
	while True:
		istemcidenGelenMesaj = baglanti.recv(Buffer_Boyutu)
		if not istemcidenGelenMesaj:
			break
		print ("Istemciden mesaj geldi: ", istemcidenGelenMesaj)
		print ("Istemciden mesaj alindi ve Buffer bosaldi.", baglantiAdedi, "nolu istemci ile baglanti kesiliyor...")
		#baglanti.send(". baglantiyi kuran istemciydiniz. Baglandiginiz icin tesekkurler. Baglanti kesiliyor...")
	print (baglantiAdedi, "nolu istemci ile baglanti kesildi.")
	baglantiAdedi += 1
baglanti.close()
 
# Sonuc