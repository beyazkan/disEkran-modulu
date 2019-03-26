import pygame
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


    def close(self):
        return False