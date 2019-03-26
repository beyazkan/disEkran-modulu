import pygame
from utils_kit import *
from threading import *
import config as conf


class Graphic_Screen(Thread):
    screen = ""
    resolution = (conf.pencere_width, conf.pencere_height)
    done = False
    clock = pygame.time.Clock()
    font = ""
    def __init__(self, hasta):
        self.hasta = hasta
        Thread.__init__(self)
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(conf.title)
        self.font = pygame.font.Font('.\\asset\Open_Sans\OpenSans-Bold.ttf', 32)


    def run(self):
        print(self.hasta)
        """
        if self.hasta.len() >= 0:
            baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
            hekim_adi = upper(self.hasta[3])
            hasta_bilgi_text = "HASTA"
            hasta_sire_bilgi = self.hasta[2]
            hasta_adi_bilgi = upper(self.hasta[1])
        else: """
        baslik_yazisi = upper("Ağız ve Çene Cerrahisi Kliniği")
        hekim_adi = upper("hasta[3]")
        hasta_bilgi_text = "HASTA"
        hasta_sire_bilgi = "hasta[2]"
        hasta_adi_bilgi = upper("hasta[1]")
        self.text = self.font.render(baslik_yazisi, True, hex_to_rgb('#F44336'))
        self.hekim_text = self.font.render(hekim_adi, True, hex_to_rgb('#FFFFFF'))
        self.hasta_bilgi = self.font.render(hasta_bilgi_text, True, hex_to_rgb('#FFFFFF'))
        self.hasta_adi = self.font.render("({}) {}".format(1, hasta_adi_bilgi), True, hex_to_rgb('#000000'))
        #print(pygame.font.get_fonts())
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Üst Doktor
            self.rect1 = pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 0, 800, 100))
            self.rect2 = pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 100, 180, 140))
            self.rect3 = pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 100, 620, 140))
            self.screen.blit(self.text, (400 - self.text.get_width() // 2, 25 - self.text.get_height() // 2))
            self.screen.blit(self.hekim_text, (400 - self.hekim_text.get_width() // 2, 70 - self.hekim_text.get_height() // 2))
            self.screen.blit(self.hasta_bilgi, (85 - self.hasta_bilgi.get_width() // 2, 170 - self.hasta_bilgi.get_height() // 2))
            self.screen.blit(self.hasta_adi, (290 - self.hasta_bilgi.get_width() // 2, 170 - self.hasta_bilgi.get_height() // 2))
            # Alt Doktor
            self.rect4 = pygame.draw.rect(self.screen, hex_to_rgb('#1976D2'), pygame.Rect(0, 240, 800, 100))
            self.rect5 = pygame.draw.rect(self.screen, hex_to_rgb('#00BCD4'), pygame.Rect(0, 340, 180, 140))
            self.rect6 = pygame.draw.rect(self.screen, hex_to_rgb('#FFFFFF'), pygame.Rect(180, 340, 620, 140))
            self.screen.blit(self.text, (400 - self.text.get_width() // 2, 265 - self.text.get_height() // 2))
            self.screen.blit(self.hekim_text, (400 - self.hekim_text.get_width() // 2, 310 - self.hekim_text.get_height() // 2))
            self.screen.blit(self.hasta_bilgi, (85 - self.hasta_bilgi.get_width() // 2, 410 - self.hasta_bilgi.get_height() // 2))
            self.screen.blit(self.hasta_adi, (290 - self.hasta_bilgi.get_width() // 2, 410 - self.hasta_bilgi.get_height() // 2))
            pygame.display.flip()
            self.clock.tick(60)

    def Intro_Scene(self):
        pass


    def close(self):
        return False