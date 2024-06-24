
from django.urls import path
from .views import index, create_material
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('create_material', create_material, name='create-material'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

