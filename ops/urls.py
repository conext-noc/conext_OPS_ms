from django.urls import path
from .views import OPS, CHECK

urlpatterns = [
    path("", OPS.as_view()),
    path("check/", CHECK.as_view()),
]
