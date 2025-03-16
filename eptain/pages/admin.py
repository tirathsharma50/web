from django.contrib import admin
from .models import Page
from ckeditor.widgets import CKEditorWidget
from django import forms

class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ('title', 'author', 'status', 'visibility', 'publish_date', 'updated_at')
    list_filter = ('status', 'visibility', 'publish_date')
    search_fields = ('title', 'content', 'seo_title', 'seo_keywords')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'
