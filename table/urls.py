from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('', index, name='home')
]
