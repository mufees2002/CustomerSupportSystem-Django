# Generated by Django 4.1.4 on 2023-06-19 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stockandpurchase", "0005_purchase"),
    ]

    operations = [
        migrations.CreateModel(
            name="Details",
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
                ("descripiton", models.CharField(max_length=200)),
                ("rating", models.IntegerField(default=0)),
                (
                    "items",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ditems",
                        to="stockandpurchase.items",
                    ),
                ),
            ],
        ),
    ]
