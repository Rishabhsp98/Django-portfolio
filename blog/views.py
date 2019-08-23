from django.shortcuts import render,get_list_or_404

# Create your views here.
from .models import Blog
def allblogs(request):
    blog=Blog.objects
    return render(request,'blog/allblogs.html',{'blog':blog})

def detail(request,blog_id):
    detailblog=get_list_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})
