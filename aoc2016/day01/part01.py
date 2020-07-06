from aoc2016.models import Coordinates, Directions

eachIntersection = []
wasFound = False
bunnyHQ = None

def ParseInput(input):
    myDirections = []
    dirs = input.split(", ")
    for dir in dirs:
        parts = list(dir)
        rot = parts.pop(0)
        dis = ''.join(parts)
        #print(rot,dis)
        theDir = Directions(rotation=rot, distance=int(dis))
        myDirections.append(theDir)

    return myDirections

def FindDistance(directions: Directions):
    myPosition = Coordinates(xCoord=0, yCoord=0)
    myDirection = "N"
    for dir in directions:
        myDirection = Rotate(myDirection, dir.rotation)
        myPosition = Advance(myPosition, myDirection, dir.distance)
        print('\'' + str(dir) + '\'', 'Go ' + str(dir.distance) + myDirection + ' to', '(' + str(myPosition) + ')')

    return myPosition

def Rotate(direction, rotation):
    orthogonals = ['N', 'E', 'S', 'W']
    myPosition = orthogonals.index(direction)
    if myPosition == 3 and rotation == 'R':
        return 'N'
    elif myPosition == 0 and rotation == 'L':
        return 'W'
    elif rotation == 'R':
        return orthogonals[myPosition+1]
    else:
        return orthogonals[myPosition-1]

def Advance(coords: Coordinates, direction, distance):
    if (direction == 'N'):
        coords.yCoord += int(distance)
    elif (direction == 'E'):
        coords.xCoord += int(distance)
    elif (direction == 'S'):
        coords.yCoord -= int(distance)
    elif (direction == 'W'):
        coords.xCoord -= int(distance)
    return coords

def FindFirstRepeat(directions: Directions):    
    global wasFound
    global bunnyHQ

    myPosition = Coordinates(xCoord=0, yCoord=0)
    myDirection = "N"
    for dir in directions:
        myDirection = Rotate(myDirection, dir.rotation)
        myPosition = AdvanceByBlock(myPosition, myDirection, dir.distance)
        print('\'' + str(dir) + '\'', 'Go ' + str(dir.distance) + myDirection + ' to', '(' + str(myPosition) + ')')
    
        #if WasVisited(myPosition) == True:
        if wasFound:
            # print('So Far', eachIntersection)
            print('Right Now', myPosition)
            print('bunnyHQ', bunnyHQ)
            return bunnyHQ
            
            #eachIntersection.append(Coordinates(xCoord=myPosition.xCoord, yCoord=myPosition.yCoord))

def AdvanceByBlock(position: Coordinates, direction, distance):
    global wasFound
    global bunnyHQ

    increment = 1
    if direction == 'W' or direction == 'S':
        increment = -1

    newSpot = Coordinates(xCoord=position.xCoord, yCoord=position.yCoord)
    #print('AdvanceByBlock, newSpot', newSpot)
    for i in range(distance):
        #if distance == 189:
        #    print('each new spot', newSpot)

        if direction == 'W' or direction == 'E':
            newSpot.xCoord += increment
        else:
            newSpot.yCoord += increment

        if not wasFound and WasVisited(newSpot):
            print('WE FOUND IT!')
            wasFound = True
            bunnyHQ = Coordinates(xCoord=newSpot.xCoord, yCoord=newSpot.yCoord)

        eachIntersection.append(Coordinates(xCoord=newSpot.xCoord, yCoord=newSpot.yCoord))
    
    return newSpot

def WasVisited(position: Coordinates):
    # was = filter(lambda x: position.xCoord == x.xCoord and position.yCoord == x.yCoord, eachIntersection)
    # if len(list(was)) > 0:
    #   print('was' + str(len(list(was))), list(was))
    #   return True

    for visited in eachIntersection:
        if visited.xCoord == position.xCoord and visited.yCoord == position.yCoord:
            print('REPEAT!!!', visited, position)
            return True
    
    return False
