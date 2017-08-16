from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.core.paginator import Paginator


class QuestionManager(models.Manager):
    
    def new(self, page_number=1):
        return paginate(self, page_number)
 
    def popular(self, page_number=1):
        qs = self.order_by('rating')        
        return paginate(qs, page_number)


class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='liked')
    
    objects = QuestionManager()
    
    class Meta:
        ordering = ('-added_at',)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


def paginate(request, qs, limit=10):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    page = paginator.page(page_number)
    return page        

