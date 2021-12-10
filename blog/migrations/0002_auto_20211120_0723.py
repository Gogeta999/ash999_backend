# Generated by Django 3.2.9 on 2021-11-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='Enable'),
        ),
        migrations.AddField(
            model_name='category',
            name='notion_id',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
