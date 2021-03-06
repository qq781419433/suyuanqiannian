# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-15 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180313_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='like_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, '编辑推送'), (1, '名家撰稿')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
