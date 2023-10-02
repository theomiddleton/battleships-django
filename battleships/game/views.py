from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import random as rng

def grid_view(request):
    cells = []
    for row in range(10):
        rowCells = []
        for col in range(10):
            rowCells.append((row, col))
        cells.append(rowCells)
        randCell = rng.choice(cells[0])
        
    context = {
        'xrange': range(5),
        'cells': cells,
        randCell: 'randCell',
    }    
    
    template = loader.get_template('game/grid.html')

    return HttpResponse(template.render(context, request))

rrow = rng.randint(0, 5)
rcol = rng.randint(0, 5)


def clicked_view(request, row, column):
    print(row, column)
    return HttpResponse(f'You clicked on cell ({row}, {column}).')

