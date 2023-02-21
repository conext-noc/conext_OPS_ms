from django.urls import path
from .views import SimpleCRUD

urlpatterns = [
    path("", SimpleCRUD.as_view()),
]
