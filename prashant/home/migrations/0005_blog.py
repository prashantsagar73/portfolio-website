# Generated by Django 3.2.4 on 2021-06-27 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_timeline_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=3000)),
                ('subtitle', models.CharField(default=' ', max_length=5000)),
                ('content', models.TextField(default=' ')),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
