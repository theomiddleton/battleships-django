from django.shortcuts import render
from django.http import HttpResponse
from .forms import HighscoreForm
from .models import Highscore
from django.template import RequestContext, loader
import random as rng

def grid_view(request):
    num = 8
    if num < 7:
        div = 1.66666667
    else:
        div = 0.66666667
    cells = []
    xrange = range(num)
    for row in xrange:
        rowCells = []
        for col in xrange:
            rowCells.append((row, col))
        cells.append(rowCells)

    randomCells = []
    while len(randomCells) < num / div:
        randRow = rng.randint(0, num -1)
        randCol = rng.randint(0, num -1)
        if (randRow, randCol) not in randomCells:
            randomCells.append((randRow, randCol))
            
    num_rows = len(cells)
    num_columns = len(cells[0])

    print(num_rows, 'rows', num_columns, 'columns')
     
    print('randomCells', randomCells)

    score = request.session.get('score', 0)
    print('score', score)
    if 'score' in request.session:
        request.session['latest_score'] = score
        del request.session['score']
    

    
    #if 'score' in request.session:
    #    del request.session['score']
    
    context = {
        'xrange': xrange,
        'randomCells': randomCells,
        'score': score,
    }   
    
    template = loader.get_template('game/grid.html')

    return HttpResponse(template.render(context, request))

def reset_view(request):
    print('resetting score')
    if 'score' in request.session:
        del request.session['score']
        print('score deleted')
    return HttpResponse('Score reset')

def clicked_view(request, row, column, is_random_int):
    print(row, column, 'true' if is_random_int else 'false')

    score = request.session.get('score', 0)

    if is_random_int:
        score = score + 50
    else:
        score = score - 5

    request.session['score'] = score # store score in session
    print('score', score)

    if is_random_int:
        message = f'You clicked on cell ({row}, {column}), which was a ship.'
    else:
        message = f'You clicked on cell ({row}, {column}), which was not a ship.'
    return HttpResponse(message + f'score={score}') 

def submit_highscore(request):
    if request.method == 'POST':
        form = HighscoreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            score = form.cleaned_data['score']
            highscore = Highscore(name=name, score=score)
            highscore.save()
            return redirect('highscores')
    else:
        form = HighscoreForm()
    return render(request, 'game/submit_highscore.html', {'form': form})

def highscores(request):
    highscores = Highscore.objects.order_by('-score')[:10]
    return render(request, 'game/highscores.html', {'highscores': highscores})