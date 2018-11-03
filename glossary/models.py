from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class User(models.Model):
#     user_name = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.user_name


class Term(models.Model):
    term = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.term


class Reference(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    source = models.CharField(max_length=250)

    def __str__(self):
        return self.source


