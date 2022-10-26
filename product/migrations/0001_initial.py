# Generated by Django 4.1.2 on 2022-10-24 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField()),
                ("price", models.FloatField()),
                ("quantity", models.IntegerField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productsAccount",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
