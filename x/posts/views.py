from django.shortcuts import render
from posts.models import Post
from posts.forms import PostForm
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(is_active=True)
    return render(request, 'posts/posts_lists.html',{"posts":posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def new_post(request):

    if request.method == "POST" :
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)    
    else:
        form = PostForm()
        return  render(request, 'posts/new_post.html', {'form': form})