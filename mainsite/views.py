# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import  datetime
from django.template.loader import get_template
# Create your views here.

# def homepage(request):
#     posts = Post.objects.all()
#     post_list = list()
#     for count, post in enumerate(posts):
#         post_list.append("No,{}:" .format(str(count)) + str(post) + "<hr>")#hr分割线
#         post_list.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")#small表示小字体，br是换行
#         # post_list.append(str(post.body.encode('utf-8')) + "<br><br>")
#
#     return HttpResponse(post_list)


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


