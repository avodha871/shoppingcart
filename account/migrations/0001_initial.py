# Generated by Django 2.2 on 2021-08-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250, unique=True)),
                ('lastname', models.CharField(max_length=250, unique=True)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
