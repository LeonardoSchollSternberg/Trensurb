from django.shortcuts import render
from django.views.generic import TemplateView

#from print.models import teste_2

# Create your views here.

from django.http import HttpResponse

import mysql.connector  #conexão banco de dados
'''
class IndexView(TemplateView):
    template_name = 'print/index.html'

    def get_queryset(self):
        return teste_2.objects.all()
'''
def index(request):
    db = mysql.connector.connect(host="localhost",user="root",password="password",auth_plugin='mysql_native_password',database="Giraffe")
    cursor=db.cursor()
    cursor.execute('SELECT * FROM teste_3 ORDER BY id DESC LIMIT 1')
    lat = [row[2] for row in cursor.fetchall()]
    lat_i = int(lat[0])
    db.close()
    context = {'lat_i': lat_i}
#    return HttpResponse(lat_i)
    return render(request, 'printDB_2/index.html', context)
    
#    query_results = teste_3.objects.all()
#    return query_results