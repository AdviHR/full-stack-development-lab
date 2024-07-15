from django.urls import path
from . import views
urlpatterns = [
path('', views.fruits_and_students, name='fruits_and_students'),
]