# Generated by Django 5.0.2 on 2024-02-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspire', '0003_alter_story_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='pic',
            field=models.FileField(upload_to='img'),
        ),
    ]
