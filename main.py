from Graphic_Screen import *
from Socket_Server import *
from threading import Thread

hasta = []

t1 = Socket_Server()
hasta = t1.get_hasta()
t1.start()

t2 = Graphic_Screen(hasta)
t2.start()

while True:
    print(hasta)

