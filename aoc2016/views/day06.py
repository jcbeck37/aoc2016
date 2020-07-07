import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day06 import ParseInput, DecodeMessage

@api_view(['POST'])
def process(request):

    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/06-sample.txt')
    with open(path_to) as f:
        sample = f.read()
    sampleLines = ParseInput(sample)
    sample = DecodeMessage(sampleLines)

    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/06.txt')
    with open(path_to) as f:
        input = f.read()
    lines = ParseInput(input)
    message = DecodeMessage(lines)
    realMessage = DecodeMessage(lines, "least")
    
    return JsonResponse({
        "sample lines": len(sampleLines),
        "sample msg": sample,
        "lines": len(lines),
        "msg": message,
        "real msg": realMessage,
    }, status=200)