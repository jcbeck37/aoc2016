from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.decorators import api_view
from aoc2016.models import Coordinates
from aoc2016.day01.part01 import ParseInput, FindDistance, FindFirstRepeat

@api_view(['POST'])
def test(request):
    testBody = request.data
    input = testBody["input"]

    directionList = ParseInput(input)

    bunnyHQ = FindDistance(directionList)
    totalBlocks = abs(bunnyHQ.xCoord) + abs(bunnyHQ.yCoord)

    print('============================================')
    print('Now find part 2 actual location')

    actualBunnyHQ = FindFirstRepeat(directionList)
    actualTotalBlocks = abs(actualBunnyHQ.xCoord) + abs(actualBunnyHQ.yCoord)

    return JsonResponse({
        "input": input,
        "bunnyHQ": str(bunnyHQ),
        "blocks":totalBlocks,
        "actualBunnyHQ": str(actualBunnyHQ),
        "actualTotalBlocks":actualTotalBlocks
    }, status=200)