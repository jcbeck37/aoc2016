
def ParseInput(input):
    rooms = []
    lines = input.split("\n")
    for line in lines:
        if line != "":
            parts = line.split("[")
            seq = parts[0].split("-")
            sectorID = int(seq.pop())
            encName = "-".join(seq)
            checkSum = parts[1].split("]")[0]
            rooms.append([encName, sectorID, checkSum])

    return rooms

def CheckRooms(rooms):
    realRooms = []
    for room in rooms:
        checksum = CreateCheckSum(room[0])
        if checksum == room[2]:
            realRooms.append(room)
        # print(room[1], room[2], checksum)
    return realRooms

def SumSectors(rooms):
    sectorSum = 0
    for room in rooms:
        sectorSum += room[1]

    return sectorSum

def CreateCheckSum(encryptedName):
    letters = encryptedName.replace("-", "")
    #print(letters)
    uniqueLetters = []
    for letter in list(letters):
        finder = list(filter(lambda n: n[0] == letter, uniqueLetters))
        if len(finder) == 0:
            uniqueLetters.append([letter, 1])
        else:
            finder[0][1] += 1
    
    #print(uniqueLetters)
    sorted = SortLetterCounts(uniqueLetters)
    #print(sorted)
    checkSum = ""
    for i in range(5):
        checkSum += sorted[i][0]
    return checkSum

def SortLetterCounts(letters):
    needsSorted = True
    while needsSorted:
        needsSorted = False
        for i in range(len(letters)-1):
            tmpA = letters[i]
            tmpB = letters[i+1]
            #print(tmpA, tmpB)

            if tmpA[1] < tmpB[1]:
                needsSorted = True
                letters[i] = tmpB
                letters[i+1] = tmpA
            elif tmpA[1] == tmpB[1] and tmpA[0] > tmpB[0]:
                needsSorted = True
                letters[i] = tmpB
                letters[i+1] = tmpA
    
    return letters

# asc a (97) z (122)
def DecryptRoomNames(rooms):
    realNames = []
    for room in rooms:
        shift = room[1] % 26
        realName = ""
        for letter in list(room[0]):
            if letter == "-":
                realName += " "
            else:
                num = ord(letter) + shift
                if num > 122:
                    num = 96 + (num % 122)
                realName += chr(num)
        #print(room[0], room[1], shift, realName)
        realNames.append("(" + str(room[1]) + ") " + realName)

    return realNames        

def FindByName(rooms, text):
    return list(filter(lambda r: r.find(text) > 0, rooms))