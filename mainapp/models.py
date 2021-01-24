from django.db import models


class Person(models.Model):
    iin = models.CharField(max_length=12)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.iin
