from django.urls import path
from .views import OPS

urlpatterns = [
    path("", OPS.as_view())
]
