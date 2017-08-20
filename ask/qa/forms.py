from django import forms
from django.contrib.auth import get_user_model

from .models import Question, Answer

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        new_user = User(**self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        new_user.set_password(pwd)
        return new_user


class AskForm(forms.Form):
    title = forms.CharField(max_length=120)
    text = forms.CharField(max_length=120)

    def save(self):
        instance = Question(**self.cleaned_data)
        return instance



class AnswerForm(forms.Form):
    text = forms.CharField(max_length=120)
    question = forms.ModelMultipleChoiceField(
                     queryset=Question.objects.all())

    def save(self):
        instance = Answer(**self.cleaned_data)
        return instance
 
