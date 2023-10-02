from django.urls import path
from . import views

urlpatterns = [
    path('', views.grid_view, name='grid_view'),
    path('clicked/<int:row>/<int:column>/', views.clicked_view, name='clicked_view'),
]
