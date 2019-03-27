import pygame
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
        
        #print(pygame.font.get_fonts())
        while not done:
            if not self.q.empty():
                self.hasta = self.q.get_nowait()
            if not self.hasta:
                baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
                hekim_adi = upper("self.hasta[0]")
                hasta_bilgi_text = upper("Hasta")
                hasta_sira_bilgi = "self.hasta[2]"
                hasta_adi_bilgi = upper("self.hasta[1]")
                self.Intro_Scene()
            else:
                baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
                hekim_adi = upper(self.hasta[0])
                hasta_bilgi_text = upper("Hasta")
                hasta_sira_bilgi = self.hasta[2]
                hasta_adi_bilgi = upper(self.hasta[1])
                sound_var = Sound(self.hasta[1])

            print(self.hasta)

            Buyuk_font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 72)
            Normal_font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 60)
            Kucuk_font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 35)
            text = Buyuk_font.render(baslik_yazisi, True, hex_to_rgb('#F44336'))
            hekim_text = Normal_font.render(hekim_adi, True, hex_to_rgb('#FFFFFF'))
            hasta_bilgi = Kucuk_font.render(hasta_bilgi_text, True, hex_to_rgb('#FFFFFF'))
            hasta_adi = Normal_font.render("({}) {}".format(hasta_sira_bilgi, hasta_adi_bilgi), True, hex_to_rgb('#000000'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.cli_socket.connect()
                    self.cli_socket.send()

            # Üst Doktor
            pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 1280, 150))
            pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 150, 180, 200))
            pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 150, 1100, 200))
            self.screen.blit(text, (conf.pencere_width // 2 - text.get_width() // 2, 45 - text.get_height() // 2))
            self.screen.blit(hekim_text, (conf.pencere_width // 2 - hekim_text.get_width() // 2, 115 - hekim_text.get_height() // 2))
            self.screen.blit(hasta_bilgi, (85 - hasta_bilgi.get_width() // 2, 250 - hasta_bilgi.get_height() // 2))
            self.screen.blit(hasta_adi, ((conf.pencere_width // 2) - (hasta_adi.get_width() // 2) + 85, 240 - hasta_adi.get_height() // 2))

            # Alt Doktor
            pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 350, 1280, 150))
            pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 500, 180, 250))
            pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 500, 1100, 250))
            self.screen.blit(text, (conf.pencere_width // 2 - text.get_width() // 2, 395 - text.get_height() // 2))
            self.screen.blit(hekim_text, (conf.pencere_width // 2 - hekim_text.get_width() // 2, 460 - hekim_text.get_height() // 2))
            self.screen.blit(hasta_bilgi, (85 - hasta_bilgi.get_width() // 2, 615 - hasta_bilgi.get_height() // 2))
            self.screen.blit(hasta_adi, ((conf.pencere_width // 2) - (hasta_adi.get_width() // 2) + 85, 605 - hasta_adi.get_height() // 2))
            
            pygame.display.flip()
            clock.tick(60)

    def Intro_Scene(self):
        pass

    def First_Scene(self):
        pass

    def Second_Scene(self):
        pass

    def close(self):
        return False