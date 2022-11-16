# Generated by Django 3.2 on 2022-11-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_auto_20221116_1459"),
    ]

    operations = [
        migrations.CreateModel(
            name="userModel",
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
                ("username", models.CharField(max_length=200)),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("age", models.CharField(max_length=200)),
                ("interests", models.CharField(max_length=200)),
                ("preference", models.CharField(max_length=200)),
                ("user_type", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="userPreferenceModel",
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
            ],
        ),
        migrations.AlterField(
            model_name="blogmodel",
            name="alt_img",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="blogmodel",
            name="img",
            field=models.ImageField(upload_to="images"),
        ),
    ]
