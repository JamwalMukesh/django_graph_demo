# myapp/models.py
from django.db import models

class MyModel(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name