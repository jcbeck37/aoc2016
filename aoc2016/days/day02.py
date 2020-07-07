
def ParseInput(input):
    codes = []
    lines = input.split("\n")
    for line in lines:
        moves = list(line)
        codes.append(moves)

    return codes

def FindCode(moves):
    lines = [
        "123",
        "456",
        "789"
    ]
    keyposx = 1
    keyposy = 1
    for move in moves:
        if move == "U" and keyposy > 0:
            keyposy -= 1
        elif move == "D" and keyposy < 2:
            keyposy += 1
        elif move == "L" and keyposx > 0:
            keyposx -= 1
        elif move == "R" and keyposx < 2:
            keyposx += 1
    
    line = lines[keyposy]
    return list(line)[keyposx]

def FindRealCode(moves):
    keyposx = 0
    keyposy = 2
    for move in moves:
        tryx = keyposx
        tryy = keyposy
        if move == "U":
            tryy = keyposy - 1
        elif move == "D":
            tryy = keyposy + 1
        elif move == "L":
            tryx = keyposx - 1
        elif move == "R":
            tryx = keyposx + 1
        code = GetKeyCode(tryx, tryy)
        if code != " ":
            keyposx = tryx
            keyposy = tryy
    
    return GetKeyCode(keyposx, keyposy)

def GetKeyCode(x, y):
    lines = [
        "  1  ",
        " 234 ",
        "56789",
        " ABC ",
        "  D  "
    ]
    if x < 0 or y < 0 or x > 4 or y > 4:
        return " "
    
    return list(lines[y])[x]