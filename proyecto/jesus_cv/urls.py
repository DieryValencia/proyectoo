from django.urls import path

from .views import index

app_name = 'jesus_cv'

urlpatterns = [
    path('', index, name='index'),
]
