# Generated by Django 5.0 on 2024-02-29 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Unwind', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='music',
            name='music',
        ),
    ]
