from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Table

# Create your views here.
from rest_framework import viewsets
from .models import Table
from .serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('-date')
    serializer_class = TableSerializer

# class HomePageView(ListView):
#     model = Table
#     template_name = 'table/index.html'
#     context_object_name = 'rows'
#     paginate_by = 10

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['caption'] = 'Таблица Weblex(ТЕСТОВОЕ ЗАДАНИЕ)'
#         return context


# def index(request):
#     return render(request=request, template_name='table/index.html')
