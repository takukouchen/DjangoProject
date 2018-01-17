# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import *
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length = 70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length = 200, blank = True)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank = True)
	author = models.ForeignKey(User)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})


class Article(models.Model):
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published'),
		)

	title = models.CharField('Title', max_length = 70)
	body = models.TextField('Body')
	created_time = models.DateTimeField('Created Time', auto_now_add = True)
	last_modified_time = models.DateTimeField('Modified Time', auto_now = True)
	status = models.CharField('Article Status', max_length = 1, choices = STATUS_CHOICES)
	abstract = models.CharField('Abstract', max_length = 54, blank = True, null = True, help_text = 'Optional')
	views = models.PositiveIntegerField('View Times', default = 0)
	likes = models.PositiveIntegerField('Positive Times', default = 0)
	topped = models.BooleanField('Set Top', default = False)

	category = models.ForeignKey('Category', verbose_name = 'Category', null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-last_modified_time']
'''
class Category(models.Model):
	name = models.CharField('Class Name', max_length=20)
	created_time = models.DateTimeField('Create Time', auto_now_add = True)
	last_modified_time = models.DateTimeField('Modified Time', auto_now = True)

	def __str__(self):
		return self.name
'''