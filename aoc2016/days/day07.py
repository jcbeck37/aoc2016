import re

def HasTLS(text):
    hypernetPattern = r"^.*\[[a-z]*([a-z]{1})(?:(?!\1)([a-z]{1})\2)\1[a-z]*\].*"
    if re.search(hypernetPattern, text):
        return False

    abbaPattern = r"^.*([a-z]{1})(?:(?!\1)([a-z]{1})\2)\1.*$"
    
    if re.search(abbaPattern, text):
        return True

    return False

def CountTLS(lines):
    ips = 0
    for line in lines.split("\n"):
        if line != "" and HasTLS(line):
            # print(line)
            ips += 1
    return ips

def HasAba(text):
    letters = list(text)
    for i in range(letters - 2):
        if letters[i] != letters[i+1] and letters[i] == letters[i+2]:
            return True

    return False

def HasBab(text: str, bab):
    return text.find(bab) > -1

def HasSSL(text):
    supernets = []
    hypernets = []

    nets = text.split('[')
    supernets.append(nets.pop(0)) #(abc)[def]ghi
    for net in nets:
        parts = net.split(']') #abc]def
        hypernets.append(parts.pop(0)) #(abc)
        supernets.append(parts.pop(0)) #def

    for supernet in supernets:
        for match in re.finditer(r'(?=(\w)(\w)\1)', supernet):
            letterA = match.group(1)
            letterB = match.group(2)

            for hypernet in hypernets:
                if HasBab(hypernet, letterB + letterA + letterB):
                    return True
        
    return False

def CountSSL(lines):
    ips = 0
    for line in lines.split("\n"):
        if line != "" and HasSSL(line):
            # print(line)
            ips += 1
    return ips