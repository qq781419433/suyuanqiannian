# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-13 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180313_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gender',
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, '编辑推荐'), (1, '名家撰稿')], default=0),
        ),
    ]
