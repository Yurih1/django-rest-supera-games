# Generated by Django 4.1.6 on 2023-02-12 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='score',
            field=models.IntegerField(),
        ),
    ]
