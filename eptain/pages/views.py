from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

# ✅ List all pages (GET) and create a new page (POST)
class PageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

# ✅ Retrieve, Update, or Delete a single page (GET, PUT, PATCH, DELETE)
class PageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = "slug"  # Use slug instead of ID
