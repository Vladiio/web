from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class QuestionManager(models.Manager):
    
    def new(self):
        return self.get_queryset()[:5]
    
    def popular(self):
        return self.get_queryset().order_by('rating')


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

