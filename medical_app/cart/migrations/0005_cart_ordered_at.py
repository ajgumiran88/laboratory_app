# Generated by Django 3.0.4 on 2020-03-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200324_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered_at',
            field=models.DateTimeField(null=True),
        ),
    ]
