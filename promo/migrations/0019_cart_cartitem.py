# Generated by Django 3.2.6 on 2021-09-29 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0018_pre_order_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ตะกร้าสินค้า',
                'verbose_name_plural': 'ข้อมูลตะกร้าสินค้า',
                'db_table': 'cart',
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo.pre_order')),
            ],
            options={
                'verbose_name': 'รายการสินค้าในตะกร้า',
                'verbose_name_plural': 'ข้อมูลรายการสินค้าในตะกร้า',
                'db_table': 'cartItem',
            },
        ),
    ]