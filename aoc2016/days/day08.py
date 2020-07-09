import copy

screen = []
width = 0
height = 0

def init(w = 50, h = 6):
    global screen, width, height
    screen = []
    width = w
    height = h
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        screen.append(row)

def parseCommands(input):
    global screen, width, height
    for line in input.split("\n"):
        if line != "":
            stdin = line.split(" ")
            if stdin[0] == "rect":
                args = stdin[1].split("x")
                rect(int(args[0]), int(args[1]))
                print("rect " + args[0] + "x" + args[1])
                # draw()
            elif stdin[0] == "rotate":
                cmd = stdin[1] # column | row
                xy = int(stdin[2].split("=")[1])
                by = int(stdin[4])
                if cmd == "column":
                    rotateColumn(xy, by)
                    # print("rotate column x=" + str(xy) + " by " + str(by))
                elif cmd == "row":
                    rotateRow(xy, by)
                    # print("rotate row x=" + str(xy) + " by " + str(by))
                else:
                    print("WHAT?!")

                #draw()
            else:
                print("WHAT?!")

def countPixels():
    global screen, width, height
    pixels = 0
    for i in range(height):
        perLine = 0
        for j in range(width):
            perLine += screen[i][j]
            pixels += screen[i][j]
            #print(screen[i][j])
        print("Line " + str(i) + ": " + str(perLine))
    return pixels

def draw():
    global screen, width, height
    print("=====================SCREEN=======================")
    frame = []
    for i in range(height):
        line = ""
        for j in range(width):
            line += (".", "#")[screen[i][j] == 1]
        print(line)
        frame.append(line)
    
    return frame

def rect(x: int, y: int):
    global screen
    for i in range(y):
        for j in range(x):
            screen[i][j] = 1

def rotateColumn(x: int, p: int):
    global screen, height
    preScreen = copy.deepcopy(screen)
    for i in range(height):
        for j in range(p):
            oldY = i - (j + 1)
            if oldY < 0:
                oldY = height + oldY
            elif oldY > (height - 1):
                oldY = (height - 1) % oldY
            
            screen[i][x] = int(preScreen[oldY][x])

def rotateRow(y: int, p: int):
    global screen, width
    preScreen = copy.deepcopy(screen)
    for i in range(width):
        for j in range(p):
            oldX = i - (j + 1)
            if oldX < 0:
                oldX = width + oldX
            elif oldX > (width - 1):
                oldX = (width - 1) % oldX
            
            screen[y][i] = int(preScreen[y][oldX])