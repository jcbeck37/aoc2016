from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.decorators import api_view
from aoc2016.models import Coordinates
from aoc2016.days.day02 import ParseInput, FindCode, FindRealCode

@api_view(['POST'])
def processDay02(request):
    body = request.data
    input = body["input"]

    moves = ParseInput(input)
    codes = []
    for move in moves:
        codes.append(FindCode(move))
        
    pins = []
    for move in moves:
        pins.append(FindRealCode(move))

    return JsonResponse({
        "input": input,
        #"moves": moves,
        "code": "".join(codes),
        "bathroomCode:": "".join(pins)
    }, status=200)