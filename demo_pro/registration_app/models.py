from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Book(models.Model):

    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    cpassword = models.CharField(max_length=1000)



    def __str__(self):
        return '{}'.format(self.title)


class BookAuthor(models.Model):
    author = models.CharField(max_length=200)
