from django.shortcuts import render, get_object_or_404, redirect

from .models import Question
from .forms import AskForm, AnswerForm


def ask(request):
    form = AskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save()
            return redirect(obj.get_absolute_url())
    return render(request, 'qa/ask.html', {'form': form})   
        


def home(request):
    page = request.GET.get('page', 1)
    qs = Question.objects.new(page)
    return render(request, 'qa/home.html',
                          {'object_list': qs.object_list,
                            'page': qs})

def popular(request):
    page = request.GET.get('page', 1)
    qs = Question.objects.popular(page)
    return render(request, 'qa/popular.html', {'object_list': qs.object_list,
                                               'page': qs})

def detail(request, pk=None):
    question = get_object_or_404(Question, pk=pk)
    form = AnswerForm(request.POST)
    if request.method == "POST":
       if form.is_valid():
           obj = form.save()
           return redirect(obj.get_absolute_url())
    context = {
        'form': form,
        'object': question,
    } 
    return render(request, 'qa/question_detail.html', context)
