import pygame
<<<<<<< HEAD
from utils_kit import *
from threading import *
import config as conf


class Graphic_Screen(Thread):
    screen = ""
    resolution = (conf.pencere_width, conf.pencere_height)
    done = False
    font = ""
    def __init__(self, hasta):
        self.hasta = hasta
        Thread.__init__(self)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Dış Ekran Uygulaması')
        done = False
        clock = pygame.time.Clock()

        if self.hasta[0] > 0:
            baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
            hekim_adi = upper(self.hasta[0][0])
            hasta_bilgi_text = upper("Hasta")
            hasta_sira_bilgi = self.hasta[0][2]
            hasta_adi_bilgi = upper(self.hasta[0][1])
        else:
            baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
            hekim_adi = upper("Uzm. Dt. Ahmet Işık")
            hasta_bilgi_text = upper("Hasta")
            hasta_sira_bilgi = "23"
            hasta_adi_bilgi = upper("Mustafa Sabri OĞUZ")

        def hex_to_rgb(hex):
            hex = hex.lstrip('#')
            color = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
            return color

        font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 32)
        text = font.render(baslik_yazisi, True, hex_to_rgb('#F44336'))
        hekim_text = font.render(hekim_adi, True, hex_to_rgb('#FFFFFF'))
        hasta_bilgi = font.render(hasta_bilgi_text, True, hex_to_rgb('#FFFFFF'))
        hasta_adi = font.render("({}) {}".format(1, hasta_adi_bilgi), True, hex_to_rgb('#000000'))
        #print(pygame.font.get_fonts())
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Üst Doktor
            pygame.draw.rect(screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 800, 100))
            pygame.draw.rect(screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 100, 180, 140))
            pygame.draw.rect(screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 100, 620, 140))
            screen.blit(text, (400 - text.get_width() // 2, 25 - text.get_height() // 2))
            screen.blit(hekim_text, (400 - hekim_text.get_width() // 2, 70 - hekim_text.get_height() // 2))
            screen.blit(hasta_bilgi, (85 - hasta_bilgi.get_width() // 2, 170 - hasta_bilgi.get_height() // 2))
            screen.blit(hasta_adi, (290 - hasta_bilgi.get_width() // 2, 170 - hasta_bilgi.get_height() // 2))
            # Alt Doktor
            pygame.draw.rect(screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 240, 800, 100))
            pygame.draw.rect(screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 340, 180, 140))
            pygame.draw.rect(screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 340, 620, 140))
            screen.blit(text, (400 - text.get_width() // 2, 265 - text.get_height() // 2))
            screen.blit(hekim_text, (400 - hekim_text.get_width() // 2, 310 - hekim_text.get_height() // 2))
            screen.blit(hasta_bilgi, (85 - hasta_bilgi.get_width() // 2, 410 - hasta_bilgi.get_height() // 2))
            screen.blit(hasta_adi, (290 - hasta_bilgi.get_width() // 2, 410 - hasta_bilgi.get_height() // 2))
            pygame.display.flip()
            clock.tick(60)


    def Intro_Scene(self):
        pass

=======
import config as conf
from utils_kit import *
from threading import *
import queue
from Socket_Client import *
from sound import *

class Graphic_Screen(Thread):
    hasta = []

    def __init__(self, q):
        Thread.__init__(self)
        self.q = q
        self.cli_socket = Socket_Client()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((conf.pencere_width,conf.pencere_height), pygame.RESIZABLE)
        pygame.display.set_caption('Dış Ekran Uygulaması')
        done = False
        clock = pygame.time.Clock()
        self.Buyuk_font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 72)
        self.Normal_font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 60)
        self.Kucuk_font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 35)
        
        #print(pygame.font.get_fonts())
        while not done:
            if not self.q.empty():
                self.hasta.append(self.q.get_nowait())
            if not self.hasta:
                self.Intro_Scene()
            elif len(self.hasta) == 1:
                print(len(self.hasta))
                print(self.hasta)
                self.baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
                self.hekim_adi = upper(self.hasta[0][0])
                self.hasta_bilgi_text = upper("Hasta")
                self.hasta_sira_bilgi = self.hasta[0][2]
                self.hasta_adi_bilgi = upper(self.hasta[0][1])
                sound_var = Sound(self.hasta[0][1])
                self.First_Scene()
            else:
                self.baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
                self.hekim_adi = upper(self.hasta[1][0])
                self.hasta_bilgi_text = upper("Hasta")
                self.hasta_sira_bilgi = self.hasta[1][2]
                self.hasta_adi_bilgi = upper(self.hasta[1][1])
                sound_var = Sound(self.hasta[1][1])
                self.Second_Scene()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.cli_socket.connect()
                    self.cli_socket.send()

            pygame.display.flip()
            clock.tick(60)

    def Intro_Scene(self):
        logo = pygame.image.load('./asset/saglik_bakanligi.png')
        logo = pygame.transform.scale(logo, (conf.pencere_width, conf.pencere_height))
        self.screen.blit(logo, (0, 0))


    def First_Scene(self):
        self.text = self.Buyuk_font.render(self.baslik_yazisi, True, hex_to_rgb('#F44336'))
        self.hekim_text = self.Normal_font.render(self.hekim_adi, True, hex_to_rgb('#FFFFFF'))
        self.hasta_bilgi = self.Kucuk_font.render(self.hasta_bilgi_text, True, hex_to_rgb('#FFFFFF'))
        self.hasta_adi = self.Buyuk_font.render("({}) {}".format(self.hasta_sira_bilgi, self.hasta_adi_bilgi), True, hex_to_rgb('#000000'))
        # Üst Doktor
        pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 1280, 150))
        pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 150, 180, 590))
        pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 150, 1100, 590))
        self.screen.blit(self.text, (conf.pencere_width // 2 - self.text.get_width() // 2, 45 - self.text.get_height() // 2))
        self.screen.blit(self.hekim_text, (conf.pencere_width // 2 - self.hekim_text.get_width() // 2, 115 - self.hekim_text.get_height() // 2))
        self.screen.blit(self.hasta_bilgi, (85 - self.hasta_bilgi.get_width() // 2, 400 - self.hasta_bilgi.get_height() // 2))
        self.screen.blit(self.hasta_adi, ((conf.pencere_width // 2) - (self.hasta_adi.get_width() // 2) + 85, 400 - self.hasta_adi.get_height() // 2))

    def Second_Scene(self):
        self.text = self.Buyuk_font.render(self.baslik_yazisi, True, hex_to_rgb('#F44336'))
        self.hekim_text = self.Normal_font.render(self.hekim_adi, True, hex_to_rgb('#FFFFFF'))
        self.hasta_bilgi = self.Kucuk_font.render(self.hasta_bilgi_text, True, hex_to_rgb('#FFFFFF'))
        self.hasta_adi = self.Normal_font.render("({}) {}".format(self.hasta_sira_bilgi, self.hasta_adi_bilgi), True, hex_to_rgb('#000000'))
        # Üst Doktor
        pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 1280, 150))
        pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 150, 180, 200))
        pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 150, 1100, 200))
        self.screen.blit(self.text, (conf.pencere_width // 2 - self.text.get_width() // 2, 45 - self.text.get_height() // 2))
        self.screen.blit(self.hekim_text, (conf.pencere_width // 2 - self.hekim_text.get_width() // 2, 115 - self.hekim_text.get_height() // 2))
        self.screen.blit(self.hasta_bilgi, (85 - self.hasta_bilgi.get_width() // 2, 250 - self.hasta_bilgi.get_height() // 2))
        self.screen.blit(self.hasta_adi, ((conf.pencere_width // 2) - (self.hasta_adi.get_width() // 2) + 85, 240 - self.hasta_adi.get_height() // 2))

        # Alt Doktor
        pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 350, 1280, 150))
        pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 500, 180, 250))
        pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 500, 1100, 250))
        self.screen.blit(self.text, (conf.pencere_width // 2 - self.text.get_width() // 2, 395 - self.text.get_height() // 2))
        self.screen.blit(self.hekim_text, (conf.pencere_width // 2 - self.hekim_text.get_width() // 2, 460 - self.hekim_text.get_height() // 2))
        self.screen.blit(self.hasta_bilgi, (85 - self.hasta_bilgi.get_width() // 2, 615 - self.hasta_bilgi.get_height() // 2))
        self.screen.blit(self.hasta_adi, ((conf.pencere_width // 2) - (self.hasta_adi.get_width() // 2) + 85, 605 - self.hasta_adi.get_height() // 2))
>>>>>>> eaeb6d6e662ac69d41024afae40e552ed9063dc1

    def close(self):
        return False