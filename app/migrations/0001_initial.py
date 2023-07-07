# Generated by Django 4.2.1 on 2023-07-04 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("membership", models.CharField(max_length=100)),
                ("amount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                ("email", models.EmailField(max_length=254)),
                ("packamount", models.IntegerField()),
                (
                    "memberships",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.member"
                    ),
                ),
            ],
        ),
    ]