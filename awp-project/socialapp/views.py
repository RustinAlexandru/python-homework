from django.shortcuts import render, redirect

from socialapp.models import UserPost, UserPostComment
from socialapp.forms import UserPostForm, UserCommentForm



def index(request):
    posts = UserPost.objects.order_by('-date_added')
    if request.method == 'GET':
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            user_post = UserPost(text=text, author=author)
            user_post.save()
            return redirect('index')
        return render(request, 'index.html', {'form': form, 'posts': posts,})

def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    title = post.text[:15] + "[...]"
    comments = UserPostComment.objects.filter(post=post).order_by('-date_added')
    context = {
        'post': post,
        'title': title,
        'comments': comments,
    }
    if request.method == 'GET':
        form = UserCommentForm()
        context['form'] = form
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            user_post_comment = UserPostComment(text=text, post=post)
            user_post_comment.save()
            return redirect('post_details')
        context[form] = form
        return render(request, 'post_details.html', context)


