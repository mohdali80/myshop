# Generated by Django 4.0.4 on 2022-05-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_cartorder_options_alter_cartorderitems_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='total_amt',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
