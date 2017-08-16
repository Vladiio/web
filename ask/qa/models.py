from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):

    def new(self, page_number=1):
        qs = self.get_queryset()
        return paginate(qs, page_number)

    def popular(self, page_number=1):
        qs = self.get_queryset().order_by('-rating')
        return paginate(qs, page_number)


class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                                            related_name='liked')

    objects = QuestionManager()

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qa:detail', kwargs={'pk': self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


def paginate(qs, page_number, limit=10):
    paginator = Paginator(qs, limit)
    page = paginator.page(page_number)
    return page

