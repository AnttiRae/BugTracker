"""BugTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from app.views import BugView, ProfileView, singleBugView, HomeView, CommentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('bugs/', BugView.as_view(), name='bugs-view'),
    path('bugs/<int:pk>', singleBugView.as_view(), name='single-bug'),
    path('bugs/<int:pk>/comment', CommentsView.as_view(), name='comments'),
    path('profile/', ProfileView.as_view(), name='profile-view'),
    path('', HomeView.as_view(), name='home'),
]
