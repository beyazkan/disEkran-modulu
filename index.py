from threading import Thread
import time, os
import socket
from gtts import gTTS
import pyglet
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
import pyrr
import freetype
import pygame

time_value = 0
HOST = '127.0.0.1'
PORT = 6000

hekim = {}

done = False

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    color = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
    return color
    #glColor3f((1.0/255.0)*color[0], (1.0/255.0)*color[1], (1.0/255.0)*color[2])

def timer():
    global time_value, done
    while True:
        if done:
            print("Timer durdu")
            break
        time_value += 1
        time.sleep(1)

def server_listening():
    global done
    print("Dış Ekran Sunucusu")
    while True:
        if done:
            print("server durdu")
            break
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print ("Bağlantı Bekleniyor...")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    #conn.sendall(data)
                    stringifade = data.decode("utf-8")
                    hasta = str(stringifade).split("*")
                    print(hasta[0].strip()) # Hekim Adı
                    print(hasta[1]) # Hasta Adı
                    print(hasta[2]) # Hasta Sıra No
                    print(hasta[3]) # Ünvanlı Hekim Adı
                    print(hasta[4]) # Ünvanlı Hekim Adı
                    print(hasta[5]) # Ünvanlı Hekim Adı
                    print(hasta[6]) # Ünvanlı Hekim Adı
                    print(hasta[7]) # Ünvanlı Hekim Adı
                    print(hasta[8]) # Ünvanlı Hekim Adı
                    print(hasta[9]) # Ünvanlı Hekim Adı
                    print(hasta[10]) # Ünvanlı Hekim Adı
                    print(hasta[11]) # Ünvanlı Hekim Adı
                    print(hasta[12]) # Ünvanlı Hekim Adı
                    print(hasta[13]) # Ünvanlı Hekim Adı
                    print(hasta[14]) # Ünvanlı Hekim Adı
                    print(hasta[15]) # Ünvanlı Hekim Adı

                    tts = gTTS(hasta[1], lang='tr')
                    if not os.path.exists("./tmp"):
                        os.makedirs('./tmp/')
                    tts.save("./tmp/temp.mp3")
                    #playsound("./mp3/sound.mp3")
                    sound = pyglet.media.load('./tmp/temp.mp3', streaming = False)
                    sound.play()
                    time.sleep(sound.duration)
                    os.remove("./tmp/temp.mp3")
                    break
                conn.close()
                print(time_value)

def Pygame_Screen():
    global done
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,600))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.draw.rect(screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 800, 100))
        pygame.draw.rect(screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 100, 180, 140))
        pygame.draw.rect(screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 100, 620, 140))
        pygame.display.flip()
        clock.tick(60)
        

graphic_render = Thread(target= Pygame_Screen)
time_thread = Thread(target= timer)
server_thread = Thread(target= server_listening)

graphic_render.daemon = True
#time_thread.daemon = True
#server_thread.daemon = True

graphic_render.start()
time_thread.start()
server_thread.start()

