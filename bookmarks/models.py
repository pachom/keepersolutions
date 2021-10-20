from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    private = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title