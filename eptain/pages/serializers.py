from rest_framework import serializers
from .models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'  # Includes all fields (title, slug, content, etc.)
