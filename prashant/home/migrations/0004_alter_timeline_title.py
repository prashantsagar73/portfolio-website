# Generated by Django 3.2.3 on 2021-06-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_timeline_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
