# Generated by Django 4.0.4 on 2022-06-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]
