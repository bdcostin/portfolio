# Generated by Django 2.2.3 on 2019-07-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_python'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='challenges',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]