# Generated by Django 5.1.3 on 2024-12-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
