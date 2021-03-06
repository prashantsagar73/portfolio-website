# Generated by Django 3.2.3 on 2021-06-20 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='content',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='timeline',
            name='link',
            field=models.URLField(blank=True, db_index=True, max_length=1000, unique=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='timeline',
            name='subtitle',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AddField(
            model_name='timeline',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='timeline',
            name='title',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
