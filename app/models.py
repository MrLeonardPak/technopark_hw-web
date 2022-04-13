import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.order_by('-rating')

    def new_questions(self):
        return self.order_by('-created')

    def with_tag(self, tag):
        return self.filter(tags__name=tag)

    def single_question(self, id):
        return self.get(id=id)


class AnswerManager(models.Manager):
    def to_question(self, id):
        return self.filter(question__exact=id)


class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, default=0)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    owner = models.ForeignKey('Profile', models.CASCADE)
    question = models.ForeignKey('Question', models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    rating = models.IntegerField(blank=True, default=0)

    objects = AnswerManager()

    def __str__(self):
        return 'by ' + self.owner.user.username + ' to ' + self.question.title


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField(
        upload_to='uploads/', default='static/img/profile.png')
    user = models.OneToOneField(User, models.CASCADE)

    def __str__(self):
        return self.user.username


class LikeForQuestion(models.Model):
    owner = models.ForeignKey('Profile', models.CASCADE)
    question = models.ForeignKey('Question', models.CASCADE)
    is_like = models.BooleanField()

    def __str__(self):
        return 'by ' + self.owner.user.username + ' to ' + self.question.title

    class Meta:
        unique_together = ['owner', 'question']


class LikeForAnswer(models.Model):
    owner = models.ForeignKey('Profile', models.CASCADE)
    answer = models.ForeignKey('Answer', models.CASCADE)
    is_like = models.BooleanField()

    def __str__(self):
        return 'by ' + self.owner.user.username + ' to ' + self.answer.title

    class Meta:
        unique_together = ['owner', 'answer']
