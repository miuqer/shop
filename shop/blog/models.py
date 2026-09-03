from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('p','publish'),
        ('d','draft')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True , max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='image/')
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.title}--{self.slug}"