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
                    #playsound("./mp3/sound.mp3")
                    sound = pyglet.media.load('./tmp/temp.mp3', streaming = False)
                    sound.play()
                    time.sleep(sound.duration)
                    os.remove("./tmp/temp.mp3")
                    break
                conn.close()
                print(time_value)

def Graphic_Screen():
        # initialize glfw
    if not glfw.init():
        return
    #TODO: Pencere oluşturma kontrolünün sağlanması gerekiyor.
    monitor = glfw.get_primary_monitor()
    window = glfw.create_window(1920, 1080, "Dış Ekran", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.2, 0.3, 0.2, 1.0)
    glEnable(GL_DEPTH_TEST)
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        #Üst Panel
        #         R  G  B
        #glColor3f((1.0/255.0)*ustRenk[0], (1.0/255.0)*ustRenk[1], (1.0/255.0)*ustRenk[2])
        hex_to_rgb('#283593')
        glBegin(GL_QUADS)
        #            X    Y    Z
        glVertex3f(-1.0, 0.7, 0.0)
        glVertex3f(1.0, 0.7, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glEnd()

        #Üst Sol Panel
        hex_to_rgb('#1976D2')
        glBegin(GL_QUADS)
        glVertex3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.7, 0.0, 0.0)
        glVertex3f(-0.7, 0.7, 0.0)
        glVertex3f(-1.0, 0.7, 0.0)
        glEnd()

        #Üst Açıklama
        if time_value % 2 == 0:
            hex_to_rgb('#BDBDBD')
        else:
            hex_to_rgb('#FFFFFF')
        glBegin(GL_QUADS)
        glVertex3f(-0.7, 0.0, 0.0)
        glVertex3f(1, 0.0, 0.0)
        glVertex3f(1, 0.8, 0.0)
        glVertex3f(-0.7, 1, 0.0)
        glEnd()

        #Alt Panel
        #         R  G  B
        hex_to_rgb('#283593')
        glBegin(GL_QUADS)
        #            X    Y    Z
        glVertex3f(-1.0, -0.3, 0.0)
        glVertex3f(1.0, -0.3, 0.0)
        glVertex3f(1.0, 0, 0.0)
        glVertex3f(-1.0, 0, 0.0)
        glEnd()

        #Alt Sol Panel
        hex_to_rgb('#1976D2')
        glBegin(GL_QUADS)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(-0.7, -1.0, 0.0)
        glVertex3f(-0.7, -0.3, 0.0)
        glVertex3f(-1.0, -0.3, 0.0)
        glEnd()

        #Alt Açıklama
        if time_value % 2 == 0:
            hex_to_rgb('#BDBDBD')
        else:
            hex_to_rgb('#FFFFFF')
        glBegin(GL_QUADS)
        glVertex3f(-0.7, -1.0, 0.0)
        glVertex3f(1, -1.0, 0.0)
        glVertex3f(1, -0.3, 0.0)
        glVertex3f(-0.7, -0.3, 0.0)
        glEnd()

        glfw.swap_buffers(window)

    glfw.terminate()

def Pygame_Screen():
    global done
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.draw.rect(screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 800, 100))
        pygame.draw.rect(screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 100, 180, 140))
        pygame.draw.rect(screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 100, 620, 140))
        pygame.display.flip()
        

graphic_render = Thread(target= Pygame_Screen)
time_thread = Thread(target= timer)
server_thread = Thread(target= server_listening)

graphic_render.daemon = True
#time_thread.daemon = True
#server_thread.daemon = True

graphic_render.start()
time_thread.start()
server_thread.start()

