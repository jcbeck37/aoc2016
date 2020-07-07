
def ParseInput(input):
    triangles = []
    lines = input.split("\n")
    for line in lines:
        sides = line.split()
        if len(sides) == 3:
            triangles.append(sides)

    return triangles

def ResortTriangles(triangles):
    totalSets = len(triangles) / 3
    print(totalSets)
    actualTriangles = []
    for i in range(int(totalSets)):
        rowBase = i * 3
        for j in range(3):
            tA = triangles[rowBase][j]
            tB = triangles[rowBase+1][j]
            tC = triangles[rowBase+2][j]
            actualTriangles.append([tA, tB, tC])
    
    return actualTriangles

def FindGoodTriangles(triangles):
    goodTriangles = []
    badTriangles = []
    for triangle in triangles:
        lenA = int(triangle[0])
        lenB = int(triangle[1])
        lenC = int(triangle[2])
        if lenA + lenB <= lenC:
            badTriangles.append(triangle)
        elif lenA + lenC <= lenB:
            badTriangles.append(triangle)
        elif lenB + lenC <= lenA:
            badTriangles.append(triangle)
        else:
            goodTriangles.append(triangle)
    
    return goodTriangles