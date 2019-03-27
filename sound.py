from gtts import gTTS
import pyglet
import os, time
import threading

class Sound():
    hastaAdi = ""
    tts = ""
    folder = "tmp"
    file = "temp.mp3"
    def __init__(self, hasta_adi):
        print("Ses Kütüphanesi Yüklendi.")
        self.hastaAdi = hasta_adi
        self.tts = gTTS(self.hastaAdi, lang='tr')
        self.folder_exist()
        t1 = threading.Thread(target=self.play_sound)
        t1.daemon = True
        self.tts.save('./'+self.folder+'/'+self.file)
        t1.start()


    def folder_exist(self):
        if not os.path.exists('./'+self.folder):
            os.makedirs('./'+self.folder)
            print("{} adlı klasör oluşturuldu.".format(self.folder))

    def play_sound(self):
        uyari = pyglet.media.load('./asset/ses.wav')
        sound = pyglet.media.load('./'+self.folder+'/'+self.file, streaming = False)
        uyari.play()
        time.sleep(1)
        sound.play()
        time.sleep(sound.duration)
        os.remove('./'+self.folder+'/'+self.file)

