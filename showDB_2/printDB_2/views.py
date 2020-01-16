from django.shortcuts import get_object_or_404, render # get_object_or_404 não usado por enquanto
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse

import mysql.connector  #conexão banco de dados

import time

i=0

def index(request):
    while i!=10:
        batata(request)
        time.sleep(3)
        i=i+1

def batata(request):
    db = mysql.connector.connect(host="localhost",user="root",password="password",auth_plugin='mysql_native_password',database="Giraffe")
    cursor=db.cursor()
    cursor.execute('SELECT * FROM teste_3 ORDER BY id DESC LIMIT 1')
    lat = [row[2] for row in cursor.fetchall()]
    cursor.execute('SELECT * FROM teste_3 ORDER BY id DESC LIMIT 1')
    lon = [row[3] for row in cursor.fetchall()]
    lat_i = int(lat[0])
    lon_i = int(lon[0])
    db.close()
    context = {'lat_i': lat_i, 'lon_i': lon_i}
#    return HttpResponse(lat_i)
    return render(request, 'printDB_2/index.html', context)
