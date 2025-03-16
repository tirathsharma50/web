from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField

STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]

VISIBILITY_CHOICES = [
    ('public', 'Public'),
    ('private', 'Private'),
]

LAYOUT_CHOICES = [
    ('flex', 'Flex'),
    ('column', 'Column'),
]

class Page(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pages")
    content = RichTextField()  # Rich text field
    featured_image = models.ImageField(upload_to='pages/images/', blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True, help_text="Title for SEO (optional)")
    seo_description = models.TextField(blank=True, help_text="Meta description for SEO (optional)")
    seo_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords for SEO (optional)")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    publish_date = models.DateTimeField(default=timezone.now)

    # New Fields for Layout and Styling
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default='flex')
    custom_css = models.TextField(blank=True, help_text="Custom CSS styles")
    width = models.CharField(max_length=10, blank=True, help_text="Width in px or % (e.g., 100%, 500px)")
    height = models.CharField(max_length=10, blank=True, help_text="Height in px or % (e.g., auto, 400px)")
    margin = models.CharField(max_length=50, blank=True, help_text="CSS Margin (e.g., 10px 20px 30px 40px)")
    padding = models.CharField(max_length=50, blank=True, help_text="CSS Padding (e.g., 10px 20px 30px 40px)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/pages/{self.slug}/"
