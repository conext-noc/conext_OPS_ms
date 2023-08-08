from django.urls import path
from .views import OPS, OPSDashboard, ProgressiveResponseView

urlpatterns = [
    path("", OPS.as_view()),
    path(
        "operations/",
        OPSDashboard.as_view(),
    ),
    path("test/", ProgressiveResponseView.as_view()),
]
