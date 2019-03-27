import pygame
import config as conf
from utils_kit import *
from threading import *
import queue
from Socket_Client import *
from sound import *

class Graphic_Screen(Thread):
    dizi = list()
    doktor = list()
    islem = False

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
                self.dizi = self.q.get_nowait()

            if self.dizi:
                if not self.doktor:
                    self.doktor.append(self.dizi)
                    self.islem = True
                elif len(self.doktor) == 1:
                    if self.doktor[0][0] == self.dizi[0]:
                        self.doktor[0] = self.dizi
                        self.islem = True
                    else:
                        self.doktor.append(self.dizi)
                        self.islem = True
                elif self.doktor[0][0] == self.dizi[0]:
                    self.doktor[0] = self.dizi
                    self.islem = True
                elif self.doktor[1][0] == self.dizi[0]:
                    self.doktor[1] = self.dizi
                    self.islem = True
                else:
                    pass
                self.dizi = ""

                print(self.doktor)

            if not self.doktor:
                self.Intro_Scene()
            elif len(self.doktor) == 1:
                self.baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
                self.hekim_adi = upper(self.doktor[0][0])
                self.hasta_bilgi_text = upper("Hasta")
                self.hasta_sira_bilgi = self.doktor[0][2]
                self.hasta_adi_bilgi = upper(self.doktor[0][1])
                if self.islem:
                    sound_var = Sound(self.doktor[0][1])
                self.First_Scene()
            elif len(self.doktor) == 2:
                self.baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
                self.hekim_adi = upper(self.doktor[0][0])
                self.hasta_bilgi_text = upper("Hasta")
                self.hasta_sira_bilgi = self.doktor[0][2]
                self.hasta_adi_bilgi = upper(self.doktor[0][1])
                self.baslik_yazisi2 = upper("Ağız ve Çene Cerrahisi Kliniği")
                self.hekim_adi2 = upper(self.doktor[1][0])
                self.hasta_bilgi_text2 = upper("Hasta")
                self.hasta_sira_bilgi2 = self.doktor[1][2]
                self.hasta_adi_bilgi2 = upper(self.doktor[1][1])
                if self.islem:
                    sound_var = Sound(self.doktor[1][1])
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
        self.islem = False

    def Second_Scene(self):
        self.text = self.Buyuk_font.render(self.baslik_yazisi, True, hex_to_rgb('#F44336'))
        self.hekim_text = self.Normal_font.render(self.hekim_adi, True, hex_to_rgb('#FFFFFF'))
        self.hasta_bilgi = self.Kucuk_font.render(self.hasta_bilgi_text, True, hex_to_rgb('#FFFFFF'))
        self.hasta_adi = self.Normal_font.render("({}) {}".format(self.hasta_sira_bilgi, self.hasta_adi_bilgi), True, hex_to_rgb('#000000'))
        self.text2 = self.Buyuk_font.render(self.baslik_yazisi2, True, hex_to_rgb('#F44336'))
        self.hekim_text2 = self.Normal_font.render(self.hekim_adi2, True, hex_to_rgb('#FFFFFF'))
        self.hasta_bilgi2 = self.Kucuk_font.render(self.hasta_bilgi_text2, True, hex_to_rgb('#FFFFFF'))
        self.hasta_adi2 = self.Normal_font.render("({}) {}".format(self.hasta_sira_bilgi2, self.hasta_adi_bilgi2), True, hex_to_rgb('#000000'))
        # Üst Doktor
        pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 1280, 150))
        pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 150, 180, 200))
        pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 150, 1100, 200))
        self.screen.blit(self.text, (conf.pencere_width // 2 - self.text.get_width() // 2, 45 - self.text.get_height() // 2))
        self.screen.blit(self.hekim_text, (conf.pencere_width // 2 - self.hekim_text.get_width() // 2, 115 - self.hekim_text.get_height() // 2))
        self.screen.blit(self.hasta_bilgi, (85 - self.hasta_bilgi.get_width() // 2, 250 - self.hasta_bilgi.get_height() // 2))
        self.screen.blit(self.hasta_adi, ((conf.pencere_width // 2) - (self.hasta_adi.get_width() // 2) + 85, 240 - self.hasta_adi.get_height() // 2))
        self.islem = False

        # Alt Doktor
        pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 350, 1280, 150))
        pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 500, 180, 250))
        pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 500, 1100, 250))
        self.screen.blit(self.text2, (conf.pencere_width // 2 - self.text2.get_width() // 2, 395 - self.text2.get_height() // 2))
        self.screen.blit(self.hekim_text2, (conf.pencere_width // 2 - self.hekim_text2.get_width() // 2, 465 - self.hekim_text2.get_height() // 2))
        self.screen.blit(self.hasta_bilgi2, (85 - self.hasta_bilgi2.get_width() // 2, 615 - self.hasta_bilgi2.get_height() // 2))
        self.screen.blit(self.hasta_adi2, ((conf.pencere_width // 2) - (self.hasta_adi2.get_width() // 2) + 85, 605 - self.hasta_adi2.get_height() // 2))

    def close(self):
        return False