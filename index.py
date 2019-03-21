from threading import Thread
import time, os
import socket
from gtts import gTTS
import pyglet
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
import pyrr

time_value = 0
HOST = '127.0.0.1'
PORT = 6000

hekim = {}

def timer():
    global time_value
    while True:
        time_value += 1
        time.sleep(1)
        
def server_listening():
    print("Dış Ekran Sunucusu")
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print ("Bağlantı Bekleniyor...")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    #conn.sendall(data)
                    stringifade = data.decode("utf-8")
                    hasta = str(stringifade).split("*")
                    print(hasta[0].strip()) # Hekim Adı
                    print(hasta[1]) # Hasta Adı
                    print(hasta[2]) # Hasta Sıra No
                    print(hasta[3]) # Ünvanlı Hekim Adı
                    print(hasta[4])
                    print(hasta[5])
                    print(hasta[6])
                    print(hasta[7])
                    print(hasta[8])
                    print(hasta[9])
                    print(hasta[10])
                    print(hasta[11])
                    print(hasta[12])
                    print(hasta[13])
                    print(hasta[14])
                    print(hasta[15])
                    print(hasta[16])
                    tts = gTTS(hasta[1], lang='tr')
                    if not os.path.exists("./tmp"):
                        os.makedirs('./tmp/')
                    tts.save("./tmp/temp.mp3")
                    #playsound("./mp3/sound.mp3")
                    sound = pyglet.media.load('./tmp/temp.mp3', streaming = False)
                    sound.play()
                    time.sleep(sound.duration)
                    os.remove("./tmp/temp.mp3")
                    break
                conn.close()
                print(time_value)

def Graphic_Screen():
        # initialize glfw
    if not glfw.init():
        return
    #TODO: Pencere oluşturma kontrolünün sağlanması gerekiyor.
    window = glfw.create_window(1366, 768, "Dış Ekran", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    #        positions        colors
    cube = [-0.3, -0.3,  0.3, 1.0, 0.0, 0.0,
             0.3, -0.3,  0.3, 0.0, 1.0, 0.0,
             0.3,  0.3,  0.3, 0.0, 0.0, 1.0,
            -0.3,  0.3,  0.3, 1.0, 1.0, 1.0,

            -0.3, -0.3, -0.3, 1.0, 0.0, 0.0,
             0.3, -0.3, -0.3, 0.0, 1.0, 0.0,
             0.3,  0.3, -0.3, 0.0, 0.0, 1.0,
            -0.3,  0.3, -0.3, 1.0, 1.0, 1.0]

    cube = numpy.array(cube, dtype = numpy.float32)

    indices = [0, 1, 2, 2, 3, 0,
               4, 5, 6, 6, 7, 4,
               4, 5, 1, 1, 0, 4,
               6, 7, 3, 3, 2, 6,
               5, 6, 2, 2, 1, 5,
               7, 4, 0, 0, 3, 7]

    indices = numpy.array(indices, dtype= numpy.uint32)

    vertex_shader = """
    #version 330
    in vec3 position;
    in vec3 color;
    uniform mat4 transform;
    out vec3 newColor;
    void main()
    {
        gl_Position = transform * vec4(position, 1.0f);
        newColor = color;
    }
    """

    fragment_shader = """
    #version 330
    in vec3 newColor;
    out vec4 outColor;
    void main()
    {
        outColor = vec4(newColor, 1.0f);
    }
    """
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 192, cube, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, indices, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)


    glUseProgram(shader)

    glClearColor(0.2, 0.3, 0.2, 1.0)
    glEnable(GL_DEPTH_TEST)
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time() )
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time() )

        transformLoc = glGetUniformLocation(shader, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rot_x * rot_y)

        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    glfw.terminate()

graphic_render = Thread(target= Graphic_Screen)
time_thread = Thread(target= timer)
server_thread = Thread(target= server_listening)

graphic_render.daemon = True
#time_thread.daemon = True
#server_thread.daemon = True

graphic_render.start()
time_thread.start()
server_thread.start()

