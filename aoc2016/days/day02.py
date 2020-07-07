
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