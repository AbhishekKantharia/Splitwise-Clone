# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-23 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupId',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'GId',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('lender', models.CharField(max_length=30)),
                ('borrower', models.CharField(max_length=30)),
                ('group_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'trans',
            },
        ),
        migrations.CreateModel(
            name='UserFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('friend_user_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'UF',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=30)),
                ('group_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'UG',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(blank=True, default='default.png', null=True, upload_to=b'')),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
    ]