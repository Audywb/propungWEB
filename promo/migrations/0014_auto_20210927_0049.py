# Generated by Django 3.2.6 on 2021-09-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0013_alter_recom_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='period',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recom',
            name='period',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='registers',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registers',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]