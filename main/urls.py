from django.urls import path, include

from main.views import index_view, item_detail_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('albums/<int:pk>', item_detail_view, name='item_detail')
]
