# Generated by Django 3.2.6 on 2021-10-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0025_order_orderitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'สินค้า', 'verbose_name_plural': 'ข้อมูลสินค้าหน้ารับหิ้ว'},
        ),
        migrations.AddField(
            model_name='registers',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
