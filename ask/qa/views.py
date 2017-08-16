from django.shortcuts import render

from .models import Question


def home(request):
    page = request.GET.get('page', 1)
    qs = Question.objects.new(page)
    return render(request, 'qa/home.html', {'qa': qs.object_list,
                                            'page': qs})

def popular(request):
    page = request.GET.get('page', 1)
    qs = Question.objects.populer(page)
    return render(request, 'qa/popular.html', {'qa': qs.object_list,
                                               'page': qs})
