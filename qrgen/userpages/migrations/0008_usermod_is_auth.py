# Generated by Django 4.1.5 on 2023-06-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpages', '0007_remove_plan_scans'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermod',
            name='is_auth',
            field=models.CharField(default='None', max_length=255),
            preserve_default=False,
        ),
    ]
