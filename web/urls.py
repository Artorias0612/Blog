from django.urls import path
from .views import home
from .views import detail
from .views import blog_tag_search
from .views import blog_category_search


app_name = "web"

urlpatterns = [
    
    path('', home, name="Home"),
    path('<int:id>', detail, name="detail"),
    path('tags/<slug:tag>', blog_tag_search, name="tag"),
    path('category/<slug:category>', blog_category_search, name="category")
]
