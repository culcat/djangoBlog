from django.contrib import admin
from django.urls import path
from djangoApplication.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='djangoApplication/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('',post_list,name='home'),
    path('register/', register_view, name='register'),
    path('post/<int:post_id>',post_detail, name='post_detail'),
    path('post/edit/<int:post_id>',login_required(post_edit), name='post_edit'),
    path('post/add/',login_required(post_add), name='post_add')
]
