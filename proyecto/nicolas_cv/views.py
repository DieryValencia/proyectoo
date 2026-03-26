from django.shortcuts import render


def index(request):
    return render(request, "nicolas_cv/index.html")
