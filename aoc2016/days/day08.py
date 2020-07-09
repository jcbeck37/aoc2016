screen = []

def init():
    global screen
    for i in range(5):
        for j in range(50):
            screen[i][j] = 0

def draw():
    global screen
    frame = ""
    for i in range(5):
        line = ""
        for j in range(50):
            line += ("#", ".")[screen[i][j] == 1]
        frame += line + "\n"
    
    return frame

def rect(a, b):
    global screen
    for i in range(a):
        for j in range(b):
            screen[i][j] = 1