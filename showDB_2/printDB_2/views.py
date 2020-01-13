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
    

#    args={}
#    data = Mymodel.objects.all()
#    args['data'] = data
#    return render(request, 'index.html', args)

    db = mysql.connector.connect(host="localhost",user="root",password="password",auth_plugin='mysql_native_password',database="Giraffe")
    cursor=db.cursor()
    cursor.execute('SELECT * FROM teste_3')
    mensagem = [row[2] for row in cursor.fetchall()]
    db.close()
    return HttpResponse(mensagem)
#    return render(request, 'index.html', {'msg': mensagem})
    
#    query_results = teste_3.objects.all()
#    return query_results
'''
def index(request):
    return HttpResponse("batata")
'''