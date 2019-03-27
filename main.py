from Graphic_Screen import *
from Socket_Server import *
from threading import *
import queue

q = queue.Queue()

t1 = Socket_Server(q)
t1.start()

t2 = Graphic_Screen(q)
t2.start()
