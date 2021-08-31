from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
import re
from tags.models import Tag
from categories.models import Categorie
from django.db.models import Q
from comments.forms import CommentForm


@login_required
def post_list(request):
    posts = Post.objects.filter(owner=request.user,
                                deleted=False).order_by('-created_at')
    return render(request, 'backend/posts/list.html', {'posts': posts})


@login_required
def post_create(request):
    return render(request, 'backend/posts/create.html')


@login_required
def post_store(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data['title']
            form.cleaned_data['description']
            form.cleaned_data['content']
            form.cleaned_data['post_type']
            form.cleaned_data['front_image']
            form.cleaned_data['content_image']
            form.cleaned_data['published']
            form.cleaned_data['published_at']
            form.cleaned_data['fb_comment_url']

            post = form.save(commit=False)
            url_title = re.sub(r"[^\w\s]", '', post.title)
            url_title = re.sub(r"\s+", '_', url_title)

            post_title_exists = Post.objects.filter(url_title=url_title).first()
            if post_title_exists:
                messages.error(request, "Error: Title already exists")
            else:

                post.url_title = url_title
                post.owner = request.user
                post.save()
                messages.error(request, "Info: Post created successfully")

                return HttpResponseRedirect('/dashboard/posts')

        else:
            messages.error(request, "Error: Form not Valide")

    return render(request, 'backend/posts/create.html', {'form': form})


@login_required
def post_update(request, post_id):

    if request.method == 'POST':

        update_type = request.POST['update_type'] if 'update_type' in request.POST else "update_only"
        post = get_object_or_404(Post, pk=post_id)
        if request.FILES.get('front_image'):
            post.delete_front_image()

        if request.FILES.get('content_image'):
            post.delete_content_image()

        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():

            form.cleaned_data['title']
            form.cleaned_data['description']
            form.cleaned_data['content']
            form.cleaned_data['post_type']
            form.cleaned_data['front_image']
            form.cleaned_data['content_image']
            form.cleaned_data['published']
            form.cleaned_data['published_at']
            form.cleaned_data['fb_comment_url']

            post = form.save(commit=False)

            url_title = re.sub(r"[^\w\s]", '', post.title)
            url_title = re.sub(r"\s+", '_', url_title)
            post.url_title = url_title
            post.save()

            messages.error(request, "Info: Post updated successfully")
            if "update_continue" not in update_type:
                return HttpResponseRedirect('/dashboard/posts')

        else:
            messages.error(request, "Error: Form not Valide")

    return render(request, 'backend/posts/edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.deleted = True
    post.save()

    messages.error(request, "Info: Post deleted successfully")
    return HttpResponseRedirect('/dashboard/posts')


@login_required
def post_details(request, post_url):
    post = Post.objects.filter(url_title=post_url).order_by('-published_at').first()
    if not post:
        return HttpResponseRedirect('/dashboard/posts')
    form = CommentForm()
    return render(request, 'frontend/post_details.html', {'post': post, 'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'backend/posts/edit.html', {'post': post})


@login_required
def post_options(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    tags = post.tag_set.all()
    categories = post.categorie_set.all()
    return render(request, 'backend/posts/post_options.html', {'tags': tags, 'post': post, 'categories': categories})


@login_required
def store_tag(request, post_id):

    if request.method == 'POST':
        if "tag" in request.POST:
            tag_id = request.POST['tag']

            tag = get_object_or_404(Tag, pk=tag_id)
            post = get_object_or_404(Post, pk=post_id)

            tag.posts.add(post)
    return HttpResponseRedirect('/dashboard/posts/options/{}'.format(post_id))


@login_required
def remove_tag(request, post_id):

    if request.method == 'POST':
        if "tag" in request.POST:
            tag_id = request.POST['tag']

            tag = get_object_or_404(Tag, pk=tag_id)
            post = get_object_or_404(Post, pk=post_id)

            tag.posts.remove(post)
    return HttpResponseRedirect('/dashboard/posts/options/{}'.format(post_id))


@login_required
def store_categorie(request, post_id):

    if request.method == 'POST':
        if "categorie" in request.POST:
            categorie_id = request.POST['categorie']

            categorie = get_object_or_404(Categorie, pk=categorie_id)
            post = get_object_or_404(Post, pk=post_id)

            categorie.posts.add(post)
    return HttpResponseRedirect('/dashboard/posts/options/{}'.format(post_id))


@login_required
def remove_categorie(request, post_id):

    if request.method == 'POST':
        if "categorie" in request.POST:
            categorie_id = request.POST['categorie']

            categorie = get_object_or_404(Categorie, pk=categorie_id)
            post = get_object_or_404(Post, pk=post_id)

            categorie.posts.remove(post)
    return HttpResponseRedirect('/dashboard/posts/options/{}'.format(post_id))
