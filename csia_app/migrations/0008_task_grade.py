# Generated by Django 3.2.9 on 2021-11-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csia_app', '0007_alter_task_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='grade',
            field=models.IntegerField(null=True),
        ),
    ]
