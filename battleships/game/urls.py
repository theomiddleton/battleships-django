from django.urls import path
from . import views

urlpatterns = [
    path('', views.grid_view, name='grid_view'),
    path('clicked/<int:row>/<int:column>/<int:is_random_int>/', views.clicked_view, name='clicked_view'),
    path('grid/<int:score>/', views.grid_view, name='grid_with_score'),
]
