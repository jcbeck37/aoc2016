import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.days.day05 import CreatePassword, CreateBetterPassword

@api_view(['POST'])
def process(request):
    sampleInput = 'abc'
    samplePwd = CreatePassword(sampleInput)
    newSamplePwd = CreateBetterPassword(sampleInput)

    input = 'wtnhxymk'
    pwd = CreatePassword(input)
    newPwd = CreateBetterPassword(input)

    return JsonResponse({
        "sampleInput": sampleInput,
        "samplePwd": samplePwd,
        "newSamplePwd": newSamplePwd,
        "input": input,
        "pwd": pwd,
        "newPwd": newPwd,
    }, status=200)