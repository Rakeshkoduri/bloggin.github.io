from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def contact(request):
    return render(request, 'blog/contact.html', )


def blog_post(request, ):
    posts = Post.objects.all().order_by('-created')
    p = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = p.get_page(page_number)
    context = {
        'posts': posts,
        'page':page
    }
    return render(request, 'blog/blog.html', context,)


def blog_list(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/blog_list.html', {'post': post})
