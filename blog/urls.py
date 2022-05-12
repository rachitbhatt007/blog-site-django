from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('posts', views.PostListView.as_view(), name="all_posts"),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name="individual_post"),
    path('favourites', views.FavouriteView.as_view(), name="favourites")
]
