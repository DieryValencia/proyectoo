from django.urls import path

from .views import index

app_name = 'oskar_cv'

urlpatterns = [
    path('', index, name='index'),
]
