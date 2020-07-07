import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day03 import ParseInput, FindGoodTriangles, ResortTriangles

@api_view(['POST'])
def process(request):
    body = request.data
    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/03.txt')
    with open(path_to) as f:
        input = f.read()

    triangles = ParseInput(input)
    goodTriangles = FindGoodTriangles(triangles)
    actualTriangles = ResortTriangles(triangles)
    actualPossible = FindGoodTriangles(actualTriangles)

    return JsonResponse({
        #"input": input,
        "triangles": len(triangles),
        "possible": len(goodTriangles),
        "actual possible": len(actualPossible),
    }, status=200)