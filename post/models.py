from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(null=True, blank=True)
    number = models.DecimalField(max_digits=3, decimal_places=1)
    upload = models.FileField(upload_to=None, max_length=200, null=True)