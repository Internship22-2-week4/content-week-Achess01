from statistics import mode
from django.db import models

# from user.models import User
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    """
    Categoría model
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.description}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title} {self.image} {self.author} {self.category}'


# Author.objects.create(firs_name="J.K.", last_name="Rowling", image="data:image/jpeg;base64,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")
