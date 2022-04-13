import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManger(models.Manager):
    def hot_questions(self):
        return self.filter(rating__gt=10)

    def new_questions(self):
        return self.filter(created__date__exact=datetime.date.today())

    def rating(self):
        # TODO: Надо посчитать число лайков
        return 10


class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('Like')

    objects = QuestionManger()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    owner = models.ForeignKey('Profile', models.CASCADE)
    question = models.ForeignKey('Question', models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    likes = models.ManyToManyField('Like')


class Tag(models.Model):
    name = models.CharField(max_length=128)


class Profile(models.Model):
    avatar = models.ImageField(upload_to='uploads/')
    user = models.OneToOneField(User, models.CASCADE)


class Like(models.Model):
    owner = models.ForeignKey('Profile', models.CASCADE)
    is_like = models.BooleanField()
