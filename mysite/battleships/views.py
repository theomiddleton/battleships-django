from random import randint
from django.shortcuts import render
import json
from django.template import RequestContext, loader
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

def notindex(request):
    rrow = randint(0,5)
    rcol = randint(0,5)
    print(rrow, rcol)
    grid = [[None] * 6 for i in range(6)]
    template = loader.get_template('index.html')
    context = {
        'tgrid' : range(4), 
        'grid': grid,
        'xrange': range(0, 6),
        'yrange': range(0, 6),
        'trange': range(0, 3),
        'rows': range(1, 6),
        'cols': range(1, 6),
        'rrow': rrow,
        'rcol': rcol,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    rrow = randint(0,5)
    rcol = randint(0,5)
    randgh = randint(0,1)
    grid = [[None] * 6 for i in range(6)]
    rows = range(0, 5)
    cols = range(0, 5)
    context = {
        'irange': range(25),
        'randgh': randgh,
        'rrow': rrow,
        'rcol': rcol,
        'grid': grid,
        'rows': rows,
        'cols': cols,
    }
    return render(request, 'index.html', context)

from django.http import JsonResponse

def handle_data(request):
    if request.method == 'POST':
        row = request.POST.get('row')
        col = request.POST.get('col')
        print(f'Clicked cell: row={row}, col={col}')
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})