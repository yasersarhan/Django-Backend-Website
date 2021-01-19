from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
    all_posts = Post.objects.all()
    return render(request,'post/post_list.html',{'all_posts':all_posts}) 

def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post/post_detail.html',{'post':post})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request,'post/post_create.html',{'form':form })


def post_edit(request):
    pass
     