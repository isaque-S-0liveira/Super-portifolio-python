from django.db import models
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField(
        max_length=500, validators=[MinLengthValidator(10)]
    )
    linkedin = models.URLField(
        max_length=500, validators=[MinLengthValidator(10)]
    )
    bio = models.TextField()

    def __str__(self):
        return self.name
