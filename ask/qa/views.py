from django.shortcuts import render, get_object_or_404

from .models import Question


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
    return render(request, 'qa/question_detail.html', {'object': question})
