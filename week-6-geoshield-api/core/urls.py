from django.urls import path
from .views import IPAnalyzeView

urlpatterns = [
    path("ip/analyze/", IPAnalyzeView.as_view()),
]
