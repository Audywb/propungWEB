# Generated by Django 3.2.6 on 2021-09-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0009_rename_register_registers'),
    ]

    operations = [
        migrations.AddField(
            model_name='registers',
            name='p_play',
            field=models.CharField(default='0123456789999', max_length=13, unique=True),
        ),
    ]
