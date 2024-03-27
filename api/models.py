from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.title