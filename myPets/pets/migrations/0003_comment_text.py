# Generated by Django 5.0 on 2023-12-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
