from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('social-posts/<str:user_email>/', views.getSocialPosts, name="social-posts"),
    path('social-post-details/<str:pk>/', views.getSocialPost, name="social-post"),
]
