# Generated by Django 3.0.4 on 2020-03-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200308_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
