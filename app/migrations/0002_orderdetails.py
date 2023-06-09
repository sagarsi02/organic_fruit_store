# Generated by Django 4.2 on 2023-05-20 12:46

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderdetails',
            fields=[
                ('product_id_with_questity', models.CharField(max_length=250)),
                ('user_id', models.CharField(max_length=50)),
                ('total_fare', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
                ('number', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('order_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 20, 12, 46, 36, 737805, tzinfo=datetime.timezone.utc))),
                ('order_status', models.CharField(choices=[('Order Receive', 'Order Receive'), ('Order Packed', 'Order Packed'), ('Order Out for Delivery', 'Order Out for Delivery'), ('Order Delivered', 'Order Delivered')], default='Order Receive', max_length=50)),
            ],
        ),
    ]
