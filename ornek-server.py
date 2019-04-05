import socket  
sunucuSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = ''  
port = 15442
Buffer_Boyutu = 1024
sunucuSoketi.bind((host, port))
sunucuSoketi.listen(5)
print ("\n" + str(port), "portu acildi ve baglantilar dinleniyor" + "\n")
baglantiAdedi = 1
mesaj = ""
 
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
		print ("Istemciden mesaj geldi: ", istemcidenGelenMesaj.decode("utf-8"))
		print ("Istemciden mesaj alindi ve Buffer bosaldi.", baglantiAdedi, "nolu istemci ile baglanti kesiliyor...")
		baglanti.send("{}. baglantiyi kuran istemciydiniz.".format(baglantiAdedi).encode())
                baglanti.send("Baglandiginiz icin tesekkurler.")
                baglanti.send("Baglanti kesiliyor...")
	baglanti.close()
	print (baglantiAdedi, "nolu istemci ile baglanti kesildi.")
	baglantiAdedi += 1
