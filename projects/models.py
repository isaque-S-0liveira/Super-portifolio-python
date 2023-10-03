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


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField(
        max_length=500, validators=[MinLengthValidator(10)]
    )
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.URLField(max_length=500, blank=False)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        blank=False,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(
        Profile, related_name="certificates", blank=False
    )
