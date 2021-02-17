from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(default=slugify(title), unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
        )
    group = models.TextField(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )
