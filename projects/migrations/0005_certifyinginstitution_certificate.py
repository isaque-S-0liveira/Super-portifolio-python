# Generated by Django 4.2.3 on 2023-10-03 00:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_rename_profile_project_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="CertifyingInstitution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(3)
                        ],
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        max_length=500,
                        validators=[
                            django.core.validators.MinLengthValidator(10)
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(3)
                        ],
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "certifying_institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certificates",
                        to="projects.certifyinginstitution",
                    ),
                ),
                (
                    "profiles",
                    models.ManyToManyField(
                        related_name="certificates", to="projects.profile"
                    ),
                ),
            ],
        ),
    ]
