from random import randint
from django.shortcuts import render
from django.template import RequestContext, loader

from django.http import HttpResponse

def index(request):
    rrow = randint(0,5)
    rcol = randint(0,5)
    grid = [[None] * 6 for i in range(6)]
    template = loader.get_template('index.html')
    context = {
        'grid': grid,
        'xrange': range(0, 6),
        'yrange': range(0, 6),
        'rrow': rrow,
        'rcol': rcol,
    }
    return HttpResponse(template.render(context, request))




