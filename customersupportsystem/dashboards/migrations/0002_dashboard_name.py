# Generated by Django 4.1.4 on 2023-04-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dashboard",
            name="Name",
            field=models.CharField(default=None, max_length=32),
        ),
    ]
