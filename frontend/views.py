from django.shortcuts import render
from django.http import HttpResponse
import os.path
from posts.models import Post
from tags.models import Tag
from categories.models import Categorie
from django.http import HttpResponseRedirect
from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from frontend.decorators import track_views
from django.db.models import Q


@track_views
def index(request):

    posts_list = Post.objects.filter(deleted=False, published=True, post_type="Project").order_by('-published_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 8)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'frontend/index.html', {'posts': posts})


@track_views
def tech_snippets(request):

    posts_list = Post.objects.filter(deleted=False, published=True, post_type="Tech Snippet").order_by('-published_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 20)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'frontend/tech_snippets.html', {'posts': posts})


@track_views
def post_details(request, post_url):

    post = Post.objects.filter(url_title=post_url, published=True).order_by('-published_at').first()
    if not post:
        return HttpResponseRedirect('/')
    form = CommentForm()
    return render(request, 'frontend/post_details.html', {'post': post, 'form': form})


@track_views
def postByTag(request, tag_id):

    tag = Tag.objects.get(id=tag_id)
    posts_list = tag.posts.filter(deleted=False, published=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 8)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'frontend/index.html', {'posts': posts})


@track_views
def postByCategorie(request, categorie_id):

    categorie = Categorie.objects.get(id=categorie_id)

    posts_list = categorie.posts.filter(deleted=False, published=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 8)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'frontend/index.html', {'posts': posts})


@track_views
def aboutme(request):
    return render(request, 'frontend/aboutme.html')


@track_views
def privacy_policy(request):
    return render(request, 'frontend/privacy_policy.html')


def post_search(request):

    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if len(keyword) >= 3 and keyword not None:
            posts_list = Post.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword), Q(published=True), Q(deleted=False))

            if len(posts_list) <= 0:
                return HttpResponseRedirect('/')

            page = request.GET.get('page', 1)
            paginator = Paginator(posts_list, 8)

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            return render(request, 'frontend/index.html', {'posts': posts})

    return HttpResponseRedirect('/')
