from django.urls import path

from .views import PhotoDescriptionListView
from .views import index_view


urlpatterns = [
    path('', index_view, name='home'),

    path('photo_list', PhotoDescriptionListView.as_view(), name='photo_list'),
]
