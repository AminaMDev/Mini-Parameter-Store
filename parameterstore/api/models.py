from django.db import models

class Parameter(models.Model):
    name = models.CharField(max_length=60, blank=False)
    value = models.CharField(max_length=60, blank=False)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name
