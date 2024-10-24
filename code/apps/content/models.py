from django.db import models
from datetime import datetime
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    author = models.CharField(max_length=15, null=False, blank=False, default="")
    written_date = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    like_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"