from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    template_name = "posts/index.html"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template_name, context)


def group_posts(request, slug):
    template_name = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, template_name, context)




