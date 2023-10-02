from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import random as rng

def grid_view(request):
    cells = []
    for row in range(5):
        rowCells = []
        for col in range(5):
            rowCells.append((row, col))
        cells.append(rowCells)
        randCell = rng.choice(cells[0])
        
    context = {
        'xrange': range(5),
        'cells': cells,
        'randCell': randCell,
        'randRow': rng.randint(0, 4),
        'randCol': rng.randint(0, 4),
    }   
  
    template = loader.get_template('game/grid.html')

    return HttpResponse(template.render(context, request))

rrow = rng.randint(0, 5)
rcol = rng.randint(0, 5)


def clicked_view(request, row, column, is_random_int):
    print(row, column, is_random_int)
    if is_random_int:
        return HttpResponse(f'You clicked on cell ({row}, {column}), which was the random.')
    else:
        return HttpResponse(f'You clicked on cell ({row}, {column}), which was not the random.')
