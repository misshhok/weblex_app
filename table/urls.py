from .views import *
from rest_framework import routers
# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'rows', TableViewSet)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls
