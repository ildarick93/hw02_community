from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):

    latest = Post.objects.order_by('-pub_date')[:11]
    context = {"posts": latest}
    return render(request, "index.html", context)


def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    context = {"group": group, "posts": posts}
    return render(request, "group.html", context)
