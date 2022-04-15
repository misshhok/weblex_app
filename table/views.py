from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.


# class HomePageView(ListView):
#     template_name = 'table/index.html'

def index(request):
    return render(request=request, template_name='table/index.html')
