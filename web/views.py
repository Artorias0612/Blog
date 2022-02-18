from django.shortcuts import render
from .models import Blog
from .models import Tag
from .models import Category
from .models import Comments
from .forms import CommentsForm
# Create your views here.


def home(request):

    blog_posts = Blog.objects.all()

    context = {

        "post": blog_posts

    }

    return render(request,  "Home.html", context)


def detail(request, id):

    selected_post = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=selected_post)
    recents = Blog.objects.all().order_by('-created_time')[:5]
    categorys = Category.objects.all()
    comments = Comments.objects.all().filter(blog=selected_post)

    if request.method == "POST":

        form = CommentsForm(request.POST)

        if form.is_valid():

            n_name = form.cleaned_data['name']
            n_email = form.cleaned_data['email']
            n_message = form.cleaned_data['message']

            new_comment = Comments(blog=selected_post, name=n_name, email=n_email, message=n_message)
            new_comment.save()

    context = {

        'post': selected_post,
        'tags': tags,
        'recents': recents,
        'category': categorys,
        'comments': comments
    }

    return render(request, "detail.html", context)

def blog_tag_search(request, tag):

    blog_posts = Blog.objects.filter(tags__slug=tag)

    context = {

        "post": blog_posts

    }

    return render(request,  "Home.html", context)

def blog_category_search(request, category):

    blog_posts = Blog.objects.filter(category__english_title=category)

    context = {

        "post": blog_posts

    }

    return render(request,  "Home.html", context)

def Search_in_Posts(request):

    pass