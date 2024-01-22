from django.urls import path
from .views import BlogLisView, BlogCreateView, BlogDetailView


app_name="blog"
urlpatterns=[
    path('',BlogLisView.as_view(),name="home"),
    path('create/',BlogCreateView.as_view(),name="create"),
    path("<int:pk>/",BlogDetailView.as_view(),name="detail")
]