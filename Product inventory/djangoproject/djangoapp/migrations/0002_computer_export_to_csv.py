# Generated by Django 3.0.3 on 2020-09-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
    ]