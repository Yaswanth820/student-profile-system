# Generated by Django 4.1 on 2022-08-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['college_id'], name='customuser__college_518644_idx'),
        ),
    ]
