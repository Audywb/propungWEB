# Generated by Django 3.2.6 on 2021-09-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0012_recom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recom',
            name='price',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]