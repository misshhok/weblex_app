from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Table

# Create your views here.


class HomePageView(ListView):
    model = Table
    template_name = 'table/index.html'
    context_object_name = 'rows'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caption'] = 'Таблица Weblex(ТЕСТОВОЕ ЗАДАНИЕ)'
        return context


# def index(request):
#     return render(request=request, template_name='table/index.html')
