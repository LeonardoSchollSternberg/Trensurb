from django.urls import path

from . import views

app_name = 'printDB_2'
urlpatterns = [
    path('', views.batata, name='index'),
]