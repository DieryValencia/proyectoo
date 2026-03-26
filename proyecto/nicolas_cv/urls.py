from django.urls import path

from .views import index

app_name = "nicolas_cv"

urlpatterns = [
    path("", index, name="index"),
]
