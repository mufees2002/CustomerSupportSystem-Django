# Generated by Django 4.1.4 on 2023-01-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0004_registration_email_registration_lastname_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="DOB",
            field=models.CharField(default="SOME STRING", max_length=200),
        ),
    ]
