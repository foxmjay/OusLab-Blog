from posts.models import Post
from tags.models import Tag
from categories.models import Categorie


def recent_posts(request):
    posts = Post.objects.filter(published=True, deleted=False).order_by('-published_at')[:4]
    return {'recent_posts': posts}


def tag_list(request):
    tags = Tag.objects.all()
    return {'tag_list': tags}


def categorie_list(request):
    categories = Categorie.objects.all()
    return {'categorie_list': categories}


def post_types(request):
    return {'post_types': ['None', 'Project', 'Tech Snippet']}
