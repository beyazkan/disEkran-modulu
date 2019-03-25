import Graphic_Screen
from Socket_Server import *
from threading import Thread

hasta = []

def server():
    global hasta
    socketServer = Socket_Server()
    socketServer.start()
    hasta = socketServer.get_dizi()

server_thread = Thread(target= server)
server_thread.start()


