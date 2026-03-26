from django.shortcuts import render


def index(request):
    return render(request, 'oskar_cv/index.html')
