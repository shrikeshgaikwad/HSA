"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings     
from django.conf.urls.static import static
from app1.views import *
from practice.views import * 
import json
from django.http import JsonResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('home/',home,name="home"),
    path('signup/',signup,name="signup"),
    path('login/',login_page,name="login"),
    path('studentProfile/',studentProfile,name="Student Profile"),
    path('courses/',courses,name="courses"),
    path('about/',about,name="about"),
    path('notes/',notes_page,name="notes"),

    path('contact/',contact,name="contact"),
    path('result/',result,name="result"),
    path('logout/',logout_view,name="logout"),

    path('updatemarks/', update_marks, name='update_marks'),
    path('addEvent/', add_event, name='add_event'),
    path('events/',event_gallery,name="gallery"),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),





]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)