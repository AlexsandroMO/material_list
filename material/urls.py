
from django.urls import path
from .views import index, create_material, list_material, view_table, new_action
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('create_material', create_material, name='create-material'),
    path('list_material', list_material, name='list-material'),
    path('view_table', view_table, name='view-table'),
    path('new_action', new_action, name='new-action'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

