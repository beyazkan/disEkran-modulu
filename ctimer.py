import time
from threading import *
import queue

class CTimer(Thread):
    time_value = 0
    
    def __init__(self, q_time, q_done):
        Thread.__init__(self)
        self.q_time = q_time
        self.q_done = q_done
        print("Timer Sınıf Yüklendi.")
    
    def run(self):
        print("Timer Başlatıldı.")
        while not self.q_done.get():
            self.time_value += 1
            self.q_time = self.time_value
            time.sleep(1)

    def stop(self):
        self.q_done.put(True)
        print("Timer Durduruldu.")

    def get_timer(self):
        return self.time_value