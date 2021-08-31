from django.shortcuts import render
from .models import Comment
from posts.models import Post
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
import re
from django.utils.crypto import get_random_string


@login_required
def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'backend/comments/list.html', {'comments': comments})


def comment_store(request, post_id):
    if request.method == 'POST':

        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():

            form.cleaned_data['username']
            form.cleaned_data['email']
            form.cleaned_data['message']

            comment = form.save(commit=False)
            comment.post = post
            comment.stringid = get_random_string(length=32)
            comment.data = request.META.get('REMOTE_ADDR')
            comment.save()

            messages.error(request, "Info: Comment added successfully")
            return HttpResponseRedirect('/posts/{}'.format(post.url_title))

        else:
            messages.error(request, "Error: Form not Valide")

    return render(request, 'frontend/post_details.html', {'post': post, 'form': form})


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.error(request, "Info: Comment deleted successfully")
    return HttpResponseRedirect('/dashboard/comments')
