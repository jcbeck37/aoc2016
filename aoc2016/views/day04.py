import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day04 import ParseInput, CheckRooms, SumSectors, DecryptRoomNames, FindByName

@api_view(['POST'])
def process(request):
    body = request.data
    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/04.txt')
    with open(path_to) as f:
        input = f.read()

    rooms = ParseInput(input)
    realRooms = CheckRooms(rooms)
    sectorSum = SumSectors(realRooms)
    realNames = DecryptRoomNames(realRooms)
    objective = FindByName(realNames, 'north')

    return JsonResponse({
        "rooms": len(rooms),
        "real rooms": len(realRooms),
        "sector ID sum": sectorSum,
        "objective": objective,
        #"real names": realNames
    }, status=200)