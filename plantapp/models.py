from django.db import models


class product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.title)
