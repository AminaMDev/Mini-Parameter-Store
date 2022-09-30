from django.db import models


class Parameter(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    value = models.CharField(max_length=256, blank=False)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name
