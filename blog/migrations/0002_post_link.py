# Generated by Django 4.1.5 on 2023-01-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
