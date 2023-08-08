from django.urls import path
from .views import OPS, OPSDashboard

urlpatterns = [
    path("", OPS.as_view()),
    path("operations/", OPSDashboard.as_view()),
]
