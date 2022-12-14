# Generated by Django 4.1 on 2022-11-01 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("withdrawn", models.IntegerField(default=0)),
                ("total_campaign", models.IntegerField(default=0)),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
