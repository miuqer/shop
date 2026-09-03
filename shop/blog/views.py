from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    post = Post.objects.filter(status = 'p').order_by('-publish')
    context = {
        'post':post
    }
    return render(request , 'index.html' , context)

def singlePost(request , slug):
    single = get_object_or_404(Post , slug=slug , status ='p')
    context = {
        'single':single
    }
    return render(request , 'singlePost.html' , context)
def sum2(request, number):
    num = 2
    total = num + number
    context = {'result': total}
    return render(request, 'test.html', context)
    
