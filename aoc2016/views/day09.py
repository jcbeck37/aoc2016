import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day09 import decompress, decompress2

@api_view(['POST'])
def process(request):
    # tests()
    #tests2()
    #part1 = getLength()
    part2 = getLength2()

    return JsonResponse({
        #"testing": True,
        #"length": part1,
        "length2": part2,
    }, status=200)

def tests():
    print("ADVENT => " + decompress("ADVENT"))
    print("A(1x5)BC => " + decompress("A(1x5)BC"))
    print("(3x3)XYZ => " + decompress("(3x3)XYZ"))
    print("A(2x2)BCD(2x2)EFG => " + decompress("A(2x2)BCD(2x2)EFG"))
    print("(6x1)(1x3)A => " + decompress("(6x1)(1x3)A"))
    print("X(8x2)(3x3)ABCY => " + decompress("X(8x2)(3x3)ABCY"))

def getLength():
    input = load()
    decompressed = decompress(input)
    return len(decompressed)

def tests2():
    print("(3x3)XYZ => " + str(decompress2("(3x3)XYZ")))
    print("X(8x2)(3x3)ABCY => " + str(decompress2("X(8x2)(3x3)ABCY")))
    print("(27x12)(20x12)(13x14)(7x10)(1x12)A => " + str(decompress2("(27x12)(20x12)(13x14)(7x10)(1x12)A")))
    print("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN => " + str(decompress2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")))

def getLength2():
    input = load()
    return str(decompress2(input))

def load():
    # get real input
    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/09.txt')
    with open(path_to) as f:
        input = f.read()

    return input
