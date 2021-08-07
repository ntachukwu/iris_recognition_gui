from django.db import models


class EnrollModel(models.Model):
    name = models.CharField(max_length=20)
    no_files = models.IntegerField(default=0)
    enrollment_time = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
