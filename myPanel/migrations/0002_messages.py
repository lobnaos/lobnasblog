# Generated by Django 4.2.1 on 2023-05-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myPanel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Messages",
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
                ("name", models.CharField(max_length=100)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("email", models.CharField(max_length=200)),
                ("content", models.TextField()),
            ],
        ),
    ]
