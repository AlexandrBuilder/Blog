# Generated by Django 2.0.8 on 2020-06-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200609_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='annotation',
            field=models.TextField(default='', max_length=400),
        ),
    ]
