from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    views = models.CharField(max_length=50)

    def __str__(self):
        return self.question
