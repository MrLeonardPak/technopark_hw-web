from multiprocessing import context
from django.shortcuts import render

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
        "number": i
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
    } for i in range(4)
]


def index(request):
    return render(request, "index.html", {"questions": QUESTIONS})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def question(request, i: int):
    context = {
        "question": QUESTIONS[i],
        "answers": ANSWERS
    }
    return render(request, "question.html", context)
