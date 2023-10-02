from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def grid_view(request):
    template = loader.get_template('game/grid.html')
    context = {
        'xrange': range(5),
    }
    return HttpResponse(template.render(context, request))

def clicked_view(request, row, column):
    print(row, column)
    return HttpResponse(f'You clicked on cell ({row}, {column}).')
