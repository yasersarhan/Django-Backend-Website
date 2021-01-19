from django.db import models
from django.utils import timezone
CATEGORY_CHOICES = (
    ('WB','Web Development'),
    ('DB','Desktop Development'), 
    ('DS','Data Sience'),
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(null=False, default=True)
    email = models.EmailField(max_length=254, null=True, blank=True, default='Test@')
    views_count = models.PositiveIntegerField(default=0, null=True)
    category = models.CharField(
        max_length=30, 
        choices= CATEGORY_CHOICES, 
        default='Web Development'
        )

    def __str__(self):
        return self.title