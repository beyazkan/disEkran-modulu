from gtts import gTTS
import pyglet
import os
import time

class Sound():
    hastaAdi = ""
    tts = ""
    folder = "tmp"
    file = "temp.mp3"
    def __init__(self,hasta_adi):
        print("Ses Kütüphanesi Yüklendi.")
        self.hastaAdi = hasta_adi
        self.tts = gTTS(self.hastaAdi, lang='tr')
        self.folder_exist()
        self.tts.save('./'+self.folder+'/'+self.file)
        self.play_sound()


    def folder_exist(self):
        if not os.path.exists('./'+self.folder):
            os.makedirs('./'+self.folder)
            print("{} adlı klasör oluşturuldu.".format(self.folder))

    def play_sound(self):
        sound = pyglet.media.load('./'+self.folder+'/'+self.file, streaming = False)
        sound.play()
        time.sleep(sound.duration)
        os.remove('./'+self.folder+'/'+self.file)

