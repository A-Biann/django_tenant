# Generated by Django 3.2.5 on 2023-09-17 15:00

import core.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230917_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.helpers.upload_handle, verbose_name='圖片'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品圖片說明')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.helpers.upload_handle, verbose_name='圖片')),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image_set', to='products.product')),
            ],
            options={
                'verbose_name': '商品圖片',
                'verbose_name_plural': '商品圖片',
                'ordering': ['order'],
            },
        ),
    ]
