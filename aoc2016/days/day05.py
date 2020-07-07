import hashlib

def CreateHash(text):
    m = hashlib.md5(text.encode()).digest()
    return m

def CreateHexHash(text):
    m = hashlib.md5(text.encode()).hexdigest()
    return m

def CreatePassword(text):
    isComplete = False
    idx = 0
    pwd = ""
    while not isComplete:
        hexed = CreateHexHash(text + str(idx))
        if hexed[:5] == "00000":
            pwd += hexed[5:6]
            print(pwd)
            if len(pwd) == 8:
                isComplete = True
        idx += 1

    return pwd

def CreateBetterPassword(text):
    isComplete = False
    idx = 0
    pwd = ["", "", "", "", "", "", "", ""]
    found = 0
    while not isComplete:
        hexed = CreateHexHash(text + str(idx))
        if hexed[:5] == "00000" and hexed[5:6].isnumeric():
            pos = int(hexed[5:6])
            if pos >= 0 and pos <= 7 and pwd[pos] == "":
                pwd[pos] = hexed[6:7]
                found += 1
                print("".join(pwd))

            if found == 8:
                isComplete = True
        idx += 1

    return "".join(pwd)