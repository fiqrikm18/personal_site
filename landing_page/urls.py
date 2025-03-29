from django.urls import path
from .views import LandingPageView, get_portfolio_detail

urlpatterns = [
    path('', LandingPageView.as_view()),
    path('portfolio/<int:pk>/', get_portfolio_detail),
]
