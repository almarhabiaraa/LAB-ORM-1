from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from blog.models import Post 

# Create your views here.

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, content=content)
        return redirect('home')

    return render(request, 'main/add_post.html')