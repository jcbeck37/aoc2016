import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from aoc2016.settings import BASE_DIR
from aoc2016.days.day07 import HasTLS, CountTLS, HasSSL, CountSSL

@api_view(['POST'])
def process(request):
    print('abba[mnop]qrst', HasTLS('abba[mnop]qrst'))
    print('abcd[bddb]xyyx', HasTLS('abcd[bddb]xyyx'))
    print('aaaa[qwer]tyui', HasTLS('aaaa[qwer]tyui'))
    print('ioxxoj[asdfgh]zxcvbn', HasTLS('ioxxoj[asdfgh]zxcvbn'))

    path_to = os.path.join(BASE_DIR, 'aoc2016/inputs/07.txt')
    with open(path_to) as f:
        input = f.read()
    ips = CountTLS(input)
    
    print('aba[bab]xyz', HasSSL('aba[bab]xyz'))
    print('xyx[xyx]xyx', HasSSL('xyx[xyx]xyx'))
    print('aaa[kek]eke', HasSSL('aaa[kek]eke'))
    print('zazbz[bzb]cdb', HasSSL('zazbz[bzb]cdb'))

    sslIps = CountSSL(input)

    return JsonResponse({
        "IP addresses supporting TLS": ips,
        "IP addresses supporting SSL": sslIps,
    }, status=200)