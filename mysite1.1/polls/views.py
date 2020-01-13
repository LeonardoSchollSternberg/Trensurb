from django.shortcuts import render
from django.http import Http404
#3 from django.http import HttpResponse
#3 from django.template import loader

# python manage.py runserver

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#1    output = ', ' .join([q.question_text for q in latest_question_list]) # <br/> para pular linha (igual ao /n)
#1    return HttpResponse(output)
#2    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
#2    return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) #3

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
