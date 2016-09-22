# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServerNowStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.ServerInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='servernowstatus',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.ServerStatus'),
        ),
    ]
