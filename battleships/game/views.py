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

    randomCells = []
    while len(randomCells) < 3:
        randRow = rng.randint(0, 4)
        randCol = rng.randint(0, 4)
        if (randRow, randCol) not in randomCells:
            randomCells.append((randRow, randCol))
            
    num_rows = len(cells)
    num_columns = len(cells[0])

    print('num_rows', num_rows, 'num_columns', num_columns)
            
    randomRows = rng.sample(range(num_rows), 5)
    randomColumns = rng.sample(range(num_columns), 5)
        
    print('randomCells', randomCells)
    print('randomRows', randomRows)  
    print('randomColumns', randomColumns)  
    
    context = {
        'xrange': xrange,
        'cells': cells,
        'randRow': randRow,
        'randCol': randCol,
        'randomRows': randomRows,
        'randomColumns': randomColumns,
    }   
  
    template = loader.get_template('game/grid.html')

    return HttpResponse(template.render(context, request))

def clicked_view(request, row, column, is_random_int):
    print(row, column, 'true' if is_random_int else 'false')
    if is_random_int:
        return HttpResponse(f'You clicked on cell ({row}, {column}), which was the random.')
    else:
        return HttpResponse(f'You clicked on cell ({row}, {column}), which was not the random.')
