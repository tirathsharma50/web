from django.urls import path
from .views import PageListCreateAPIView, PageRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/pages/', PageListCreateAPIView.as_view(), name='api-page-list-create'),
    path('api/pages/<slug:slug>/', PageRetrieveUpdateDestroyAPIView.as_view(), name='api-page-detail'),
]
