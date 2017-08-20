from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import Question
from .forms import (
    AskForm,
    AnswerForm,
    RegisterForm,
    LoginForm,
)

User = get_user_model()


def ask(request):
    form = AskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save()
            obj.author = request.user
            obj.save()
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
           obj.author = request.user
           obj.save()
           return redirect(obj.get_absolute_url())
    context = {
        'form': form,
        'object': question,
    } 
    return render(request, 'qa/question_detail.html', context)


def register(request):
   form = RegisterForm(request.POST)
   if request.method == "POST":
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('/')
   return render(request, 'qa/register.html', {'form': form})  


def login_view(request):
    form = LoginForm(request.POST)
    error = ''
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,
                                password=password) 
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error = 'Invalid credentials'

    return render(request, 'qa/login.html', {'form': form, 'error': error})
                                              

