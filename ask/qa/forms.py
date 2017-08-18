from django import forms

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=120)
    text = forms.CharField(max_length=120)

    def save(self):
        instance = Question(**self.cleaned_data)
        instance.save()
        return instance



class AnswerForm(forms.Form):
    text = forms.CharField(max_length=120)
    question = forms.ModelMultipleChoiceField(
                     queryset=Question.objects.all())

    def save(self):
        instance = Answer(**self.cleaned_data)
        instance.save()
        return instance
 
