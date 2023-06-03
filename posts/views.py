from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView): # creating a view which inherits as a ListView
    model = Post # lists the model "Post"
    template_name = 'home.html' # uses the template "home.html"
    context_object_name = 'all_posts_list' # models stored within the view are assigned the name: 
                                           # 'all_posts_list' within the template