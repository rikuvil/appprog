# Generated by Django 4.2.7 on 2023-11-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_app', '0009_delete_gameloan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgamereview',
            name='review',
            field=models.CharField(max_length=256),
        ),
    ]
