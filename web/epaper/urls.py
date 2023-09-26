# epaper/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('epaper-base/', views.EPaperView.as_view(), name='epaper-base'),
    path('thanks/', views.EPaperThanksView.as_view(), name='thanks'),
]