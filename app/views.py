from django.core.paginator import Paginator
from django.shortcuts import render
from app.models import Question, Answer, Tag, Profile, Like

QUESTIONS = [
    {
        "title": f"Question #{i}",
        "text": '''
                I ate dinner.
                There is always a next time.
                In the end, we all felt like we ate too much.
                We all agreed; it was a magnificent evening.
                I'm confident that I'll win the tennis match.
                She opened the door.
                The car turned the corner.
                Nothing beats a complete sentence.
                She advised him to see a lawyer, so he did.
                Once you know all the elements, it's not difficult to pull together a sentence. ,
                ''',
        "id": i
    } for i in range(40)
]

ANSWERS = [
    {
        "text": f'''
                This is text for answer #{i}.
                I don't want to fail the test.
                There is always a next time.
                You were late, weren't you ?
                He denied knowing anything about their plans.
                No one can make you feel inferior without your consent.
                '''
    } for i in range(7)
]

TAGS = ["bla"*i for i in range(1, 5)]


def index(request):
    questions = paginate(Question.objects.new_questions(), request)
    context = {
        "questions": questions,
        "tags": TAGS}
    return render(request, "index.html", context)


def ask(request):
    context = {"tags": TAGS}
    return render(request, "ask.html", context)


def login(request):
    context = {"tags": TAGS}
    return render(request, "login.html", context)


def signup(request):
    context = {"tags": TAGS}
    return render(request, "signup.html", context)


def question(request, i: int):
    answers = paginate(Answer.objects.to_question(i), request, 5)
    context = {
        "question": Question.objects.single_question(i),
        "answers": answers,
        "tags": TAGS
    }
    return render(request, "question.html", context)


def hot_list(request):
    questions = paginate(Question.objects.hot_questions(), request)
    context = {
        "questions": questions,
        "tags": TAGS}
    return render(request, "hot_list.html", context)


def with_tag(request, tag: str):
    questions = paginate(Question.objects.with_tag(tag), request)
    context = {
        "tag": tag,
        "questions": questions,
        "tags": TAGS}
    return render(request, "with_tag.html", context)


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    objects_on_page = paginator.get_page(page)
    return objects_on_page
