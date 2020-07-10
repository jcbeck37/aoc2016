import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day10 import IdentifyBot, IdentifyChip, BotGetsInstructions, BotReceivesChip
from aoc2016.days.day10 import Init, Process, Summarize

@api_view(['POST'])
def process(request):
    # test1()

    input = load()
    Process(input)
    Summarize()

    return JsonResponse({
        "testing": True,
        #"length": part1,
        #"length2": part2,
    }, status=200)

def test1():
    Init()
    BotReceivesChip(2, 5)
    BotGetsInstructions(2, "bot", 1, "bot", 0)
    BotReceivesChip(1, 3)
    BotGetsInstructions(1, "output", 1, "bot", 0)
    BotGetsInstructions(0, "output", 2, "output", 0)
    BotReceivesChip(2, 2)

    # Summarize()

def load():
    # get real input
    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/10.txt')
    with open(path_to) as f:
        input = f.read()

    return input
