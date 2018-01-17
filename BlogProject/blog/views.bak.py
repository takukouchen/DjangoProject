from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import *

def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	category_list = Category.objects.all()
	return render(request, 'blog/index.html', context = {'post_list':post_list,
		'welcome':category_list},)

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/detail.html', context={'post':post})