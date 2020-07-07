from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.decorators import api_view
from aoc2016.models import Coordinates
from aoc2016.days.day02 import ParseInput, FindCode

@api_view(['POST'])
def processDay02(request):
    body = request.data
    input = body["input"]

    moves = ParseInput(input)
    codes = []
    for move in moves:
        codes.append(FindCode(move))

    return JsonResponse({
        "input": input,
        #"moves": moves,
        "codes": codes
    }, status=200)