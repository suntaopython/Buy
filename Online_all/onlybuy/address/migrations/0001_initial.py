# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-17 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consignee', models.CharField(default='any', max_length=20, verbose_name='收件人')),
                ('address', models.TextField(verbose_name='收货地址')),
                ('mobile', models.CharField(max_length=13, verbose_name='手机号')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否为默认地址')),
                ('zipcode', models.CharField(default='000000', max_length=6, verbose_name='邮编')),
                ('alias', models.CharField(max_length=50, verbose_name='别名')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]