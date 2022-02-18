from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):

    title = models.CharField(max_length=50)
    Description = models.CharField(max_length=300)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, verbose_name="Writer", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="blog/", blank=True, null=True)
    category = models.ForeignKey("Category", related_name="blog", verbose_name="category", on_delete=models.CASCADE,
                                 blank=True, null=True)
    tags = models.ManyToManyField("Tag", verbose_name="tags", related_name="blogs", blank=True, null=True)

    def __str__(self):

        return self.title


class Category(models.Model):

    title = models.CharField(max_length=50)
    english_title = models.SlugField()
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):

        return self.english_title


class Tag(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField()
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):

        return self.title



class Comments(models.Model):

    blog = models.ForeignKey("Blog", verbose_name="مقاله", related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):

        return self.email
