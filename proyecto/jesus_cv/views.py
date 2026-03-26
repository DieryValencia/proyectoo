from django.shortcuts import render


def index(request):
    return render(request, 'jesus_cv/index.html')

# Create your views here.
