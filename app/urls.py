from django.urls import include, path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
import os


urlpatterns = [
    path('home', views.home, name='home'),
    path('space_invaders', views.space_invaders, name='space_invaders'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('signup', views.signup, name='signup'),

    #path("register", views.register_request, name="register"),
    #path("login", views.register_request, name="login"),
]

STATIC_URL = 'app/static/'
STATIC_ROOT = os.path.join("", "app/static/")

STATICFILES_DIRS = (
    STATIC_ROOT,
)
