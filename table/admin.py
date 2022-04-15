from django.contrib import admin
from .models import Table
# Register your models here.


@admin.register(Table)
class WomenForm(admin.ModelAdmin):
    list_display = ('pk', 'title', 'count', 'distance', 'date')
    list_display_links = ('pk', 'title',)
    search_fields = ['title', ]
