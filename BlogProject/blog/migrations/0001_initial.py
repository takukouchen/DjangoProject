# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 08:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='Modified Time')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='Article Status')),
                ('abstract', models.CharField(blank=True, help_text='Optional', max_length=54, null=True, verbose_name='Abstract')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='View Times')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Positive Times')),
                ('topped', models.BooleanField(default=False, verbose_name='Set Top')),
            ],
            options={
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('excerpt', models.CharField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='Category'),
        ),
    ]