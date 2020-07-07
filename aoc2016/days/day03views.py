import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day03 import ParseInput, FindGoodTriangles, ResortTriangles

@api_view(['POST'])
def processDay03(request):
    body = request.data
    #input = body["input"]
    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/03.txt')
    with open(path_to) as f:
        input = f.read()

    triangles = ParseInput(input)
    goodTriangles = FindGoodTriangles(triangles)
    actualTriangles = ResortTriangles(triangles)
    actualPossible = FindGoodTriangles(actualTriangles)
    # codes = []
    # for move in moves:
    #     codes.append(FindCode(move))
        
    # pins = []
    # for move in moves:
    #     pins.append(FindRealCode(move))

    return JsonResponse({
        #"input": input,
        "triangles": len(triangles),
        "possible": len(goodTriangles),
        "actual possible": len(actualPossible),
    }, status=200)