# Generated by Django 3.2.5 on 2021-07-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='quan',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]