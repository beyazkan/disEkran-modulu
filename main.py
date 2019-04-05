from Graphic_Screen import *
from ctimer import *
from Socket_Server import *
from threading import *
import queue

q = queue.Queue()
q_time = queue.Queue()
q_done = queue.Queue()

t1 = Socket_Server(q, q_done)
t1.start()

t2 = Graphic_Screen(q, q_done)
t2.start()

t3 = CTimer(q_time, q_done)
t3.start()
