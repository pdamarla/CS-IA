# Generated by Django 3.2.9 on 2021-11-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csia_app', '0002_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(default='this is a subject'),
            preserve_default=False,
        ),
    ]
