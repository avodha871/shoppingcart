# Generated by Django 3.2.5 on 2021-07-31 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_quan'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
