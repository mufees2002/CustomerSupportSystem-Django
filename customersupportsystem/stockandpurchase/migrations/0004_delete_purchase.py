# Generated by Django 4.1.4 on 2023-04-28 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stockandpurchase", "0003_alter_items_date"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Purchase",
        ),
    ]