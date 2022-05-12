from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .models import Post,Comment
from .forms import CommentForm 
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View


class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by("-date")
        context["posts"] = posts
        return context

    # posts = Post.objects.all()
    # context = {
    #     "posts": posts
    # }
    # return render(request, 'blog/index.html', context)


class PostListView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "posts"

# def all_posts(request):
#     posts = Post.objects.all()
#     context = {
#         "posts": posts
#     }
#     return render(request, "blog/all_posts.html", context)


class PostDetailView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        favourites = request.session.get("favourites")
        if favourites !=None:
            favourite = str(post.id) in favourites
        else:
            favourites=[]
            favourite=False     

        
        context = {
            "post": post,
            "tags":post.tag.all(),
            "form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "favourite":favourite
        }
        return render(request, "blog/individual_post.html", context)
    
    def post(self,request,slug):
        form = CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        if(form.is_valid()):
            comment=form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("individual_post",args=[slug]))
        else:
            context = {
            "post": post,
            "tags":post.tag.all(),
            "form":CommentForm(),
            "comments":post.comments.all().order_by("-id")
            }
            return render(request, "blog/individual_post.html", context)


class FavouriteView(View):
    def get(self,request):
        favourites = request.session.get("favourites")
        context={}
        if favourites is None or len(favourites)==0:
            context["posts"]=[]
        else:    
            posts = Post.objects.filter(id__in = favourites)
            context["posts"]=posts
        return render(request,"blog/favourites.html",context)
    
    
    def post(self,request): 
        favourite_posts = request.session.get("favourites")
        post = request.POST["favpost"]
        if favourite_posts is None:
            favourite_posts=[]
        
        if post not in favourite_posts:
            favourite_posts.append(post)  
            request.session["favourites"]=favourite_posts
            print("favourite added")    
        else:
            favourite_posts.remove(post)
            request.session["favourites"]=favourite_posts
        print(request.session["favourites"])
        return HttpResponseRedirect(reverse("favourites"))    
