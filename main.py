from Graphic_Screen import *
from Socket_Server import *
from threading import *
import queue

<<<<<<< HEAD
hasta = []

t1 = Socket_Server()
hasta = t1.get_hasta()
t1.start()

t2 = Graphic_Screen(hasta)
t2.start()

while True:
    print(hasta)
=======
q = queue.Queue()

t1 = Socket_Server(q)
t1.start()
>>>>>>> eaeb6d6e662ac69d41024afae40e552ed9063dc1

t2 = Graphic_Screen(q)
t2.start()
