from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('handle_data/', views.handle_data, name='handle_data'),
]