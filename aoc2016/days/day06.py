def ParseInput(input):
    data = []
    lines = input.split("\n")
    for line in lines:
        if line != "":
            letters = list(line)
            data.append(letters)

    return data

def DecodeMessage(lines, mode = "most"):
    msgLength = len(lines[0])
    msg = ""
    for i in range(msgLength):
        msg += GetLetter(lines, i, mode)

    return msg

def GetLetter(lines, idx, mode):
    uniqueLetters = []
    for i in range(len(lines)):
        letter = lines[i][idx]
        finder = list(filter(lambda n: n[0] == letter, uniqueLetters))
        if len(finder) == 0:
            uniqueLetters.append([letter, 1])
        else:
            finder[0][1] += 1
    sorted = SortLetterCounts(uniqueLetters)
    if mode == "least":
        return sorted.pop()[0]
    else:
        return sorted[0][0]

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
    
    return letters
