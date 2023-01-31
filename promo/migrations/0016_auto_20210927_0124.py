# Generated by Django 3.2.6 on 2021-09-26 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0015_auto_20210927_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='slides')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ภาพสไลด์',
                'verbose_name_plural': 'ข้อมูลภาพสไลด์',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='promotion',
            name='price',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recom',
            name='image',
            field=models.ImageField(blank=True, upload_to='recom'),
        ),
        migrations.AlterField(
            model_name='recom',
            name='logo',
            field=models.ImageField(blank=True, upload_to='recom'),
        ),
        migrations.AlterField(
            model_name='recom',
            name='price',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Pre_order',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('partner_link', models.TextField(blank=True)),
                ('period', models.CharField(max_length=255)),
                ('price', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='preorder')),
                ('logo', models.ImageField(blank=True, upload_to='preorder')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo.category')),
            ],
            options={
                'verbose_name': 'สินค้ารับหิ้ว',
                'verbose_name_plural': 'ข้อมูลสินค้ารับหิ้ว',
                'ordering': ('name',),
            },
        ),
    ]
