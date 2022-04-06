from django.shortcuts import render

QUESTUINS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}"
    } for i in range(1, 10)
]

ANSWERS = [
    {
        "text": f"This is text for answer #{i}"
    } for i in range(1, 4)
]


def index(request):
    return render(request, "index.html", {"questions": QUESTUINS})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def question(request):
    return render(request, "question.html", {"answers": ANSWERS})
