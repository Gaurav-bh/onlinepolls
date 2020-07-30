from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import datetime
from django.utils import timezone
# Create your views here.
from .models import questions

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_question"
    def get_queryset(self):
        return questions.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]

"""def index(request):
    latest_question= questions.objects.order_by("-pub_date")[:5]
    context={"latest_question":latest_question}

    return render(request,"polls/index.html",context)"""
class DetailView(generic.DetailView):
        model=questions
        template_name="polls/detail.html"

        def get_queryset(self):
            return questions.objects.filter(pub_date__lte=timezone.now())





"""
def detail(request,question_id):
    question=get_object_or_404( questions,pk=question_id)
    return render(request,"polls/detail.html",{"questions":question})"""



class ResultView(generic.DetailView):
        model=questions
        template_name="polls/result.html"
"""
def result(request,question_id):
    question=get_object_or_404( questions,pk=question_id)
    return render(request,"polls/result.html",{"questions":question})"""
def vote(request,question_id):
    question=get_object_or_404(questions,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,"error_message":"you did not select a choice "})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return  HttpResponseRedirect(reverse('polls:result',args=(question_id,)))