# Generated by Django 3.2.6 on 2021-09-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0005_auto_20210914_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='partner',
        ),
        migrations.AddField(
            model_name='promotion',
            name='partner_link',
            field=models.TextField(blank=True),
        ),
    ]
