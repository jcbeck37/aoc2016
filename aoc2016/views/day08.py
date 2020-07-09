import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day08 import init, draw, rect, rotateColumn, rotateRow, parseCommands, countPixels

@api_view(['POST'])
def process(request):
    init(50, 6)
    
    input = load()
    #print(input)
    parseCommands(input)

    finalScreen = draw()
    pixels = countPixels()

    return JsonResponse({
        "screen": finalScreen,
        "pixels": pixels,
    }, status=200)

def load():
    # get real input
    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/08.txt')
    with open(path_to) as f:
        input = f.read()

    return input

def test():
    """ test case """
    init(7, 3)

    rect(3,2)
    draw()

    rotateColumn(1,1)
    draw()

    rotateRow(0, 4)
    draw()

    rotateColumn(1,1)
    test = draw()
