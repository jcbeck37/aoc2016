import copy, re

def decompress(input):
    output = ""

    compressedString = copy.copy(input)
    compressed = True
    while compressed:        
        result = re.search(r"\(\d+x\d+\)", compressedString)
        if result:
            marker = result[0]
            codeLen, codeRep = marker.replace("(","").replace(")","").split("x")

            uncompressedEndsAt = result.start(0)
            output += compressedString[:uncompressedEndsAt]
            charStart = result.start(0) + len(marker)
            
            chars = compressedString[charStart:charStart+int(codeLen)]
            expanded = chars * int(codeRep)
            
            workingText = compressedString[uncompressedEndsAt:charStart+int(codeLen)]
            compressedString = compressedString[charStart+int(codeLen):]
            output += workingText.replace(marker + chars, expanded, 1)
        else:
            compressed = False
            output += compressedString
    
    return output

def findMarker(cmp):
    return re.search(r"\(\d+x\d+\)", cmp)

def decompress2(input):
    # print('STARTING', input)
    filth = copy.copy(input)
    return innerDecompress(filth)

def innerDecompress(source):
    result = findMarker(source)
    if result:
        # decompressed text before marker
        lengthSoFar = result.start(0)

        # get marker
        marker = result[0]
        charStart = lengthSoFar + len(marker)

        # get instructions from marker
        codeLen, codeRep = marker.replace("(","").replace(")","").split("x")
        
        # split text into working set and irrelevant later stuff
        chars = source[charStart:charStart+int(codeLen)]

        # execute marker instructions        
        expansion = chars * int(codeRep)

        # print('marker, chars, rep, = ', marker, chars, codeRep, expansion)

        # len of decompressed text plus decompression of this set and decompression of later stuff
        thisLength = lengthSoFar + innerDecompress(expansion)

        # if we have later text after this set, separately decompress
        if charStart+int(codeLen) < len(source):
            extra = source[charStart+int(codeLen):]
            # print('chars, extra', chars, extra)
            # print(len(extra))
            thisLength += innerDecompress(extra)

        return thisLength
    else:
        # print('no marker in', source)
        return len(source)
