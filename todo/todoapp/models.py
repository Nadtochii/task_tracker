from django.db import models


class Task(models.Model):
    name = models.TextField()
    priority = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
