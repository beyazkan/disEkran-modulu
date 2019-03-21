#!/usr/bin/env python3

import socket
from gtts import gTTS
import os
import time
import pyglet
import glfw

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6000        # Port to listen on (non-privileged ports are > 1023)

hasta = {}

print("Dış Ekran Sunucusu")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Bağlantı Bekleniyor...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # conn.sendall(data)
            stringifade = data.decode("utf-8")
            hasta = str(stringifade).split("*")
            print(hasta[0].strip())  # Hekim Adı
            print(hasta[1])  # Hasta Adı
            print(hasta[2])  # Hasta Sıra No
            print(hasta[3])  # Ünvanlı Hekim Adı
            print(hasta[4])
            print(hasta[5])
            print(hasta[6])
            print(hasta[7])
            print(hasta[8])
            print(hasta[9])
            print(hasta[10])
            print(hasta[11])
            print(hasta[12])
            print(hasta[13])
            print(hasta[14])
            print(hasta[15])
            print(hasta[16])
            tts = gTTS(hasta[1], lang='tr')
            if not os.path.exists("./tmp"):
                os.makedirs('./tmp/')
            tts.save("./tmp/temp.mp3")
            # playsound("./mp3/sound.mp3")
            sound = pyglet.media.load('./tmp/temp.mp3', streaming=False)
            sound.play()
            time.sleep(sound.duration)
            os.remove("./tmp/temp.mp3")
            break
        conn.close()
