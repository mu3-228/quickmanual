from django.db import models


class Manual(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
