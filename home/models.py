from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='items/', blank=True, null=True)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    detailed_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/', blank=True)
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
