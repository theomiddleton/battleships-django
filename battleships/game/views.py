from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import random as rng

def grid_view(request):
    cells = []
    xrange = range(5)
    for row in xrange:
        rowCells = []
        for col in xrange:
            rowCells.append((row, col))
        cells.append(rowCells)
        randCell = rng.choice(cells[0])
        
    context = {
        'xrange': xrange,
        'cells': cells,
        'randCell': randCell,
        'randRow': rng.randint(0, 4),
        'randCol': rng.randint(0, 4),
    }   
  
    template = loader.get_template('game/grid.html')

    return HttpResponse(template.render(context, request))

def clicked_view(request, row, column, is_random_int):
    print(row, column, 'true' if is_random_int else 'false')
    if is_random_int:
        return HttpResponse(f'You clicked on cell ({row}, {column}), which was the random.')
    else:
        return HttpResponse(f'You clicked on cell ({row}, {column}), which was not the random.')
