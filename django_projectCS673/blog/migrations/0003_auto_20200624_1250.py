# Generated by Django 3.0.7 on 2020-06-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='id',
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
