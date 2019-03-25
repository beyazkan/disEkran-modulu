import time

class Timer():

    done = false
    time_value = 0

    def __init__(self):
        print("Timer Sınıf Yüklendi.")
    
    def start(self):
        print("Timer Başlatıldı.")
        while not done:
            time_value += 1
            time.sleep(1)

    def stop(self):
        self.done = True
        print("Timer Durduruldu.")

    def get_timer(self):
        return self.time_value