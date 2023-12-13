from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm

from .forns import SignUpForm, PostForm
from .models import Posts


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'djangoApplication/login.html', {'form': form})
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use password1 for the password field
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'djangoApplication/register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')

def post_list(request):
    posts = Posts.objects.all().order_by('-pub_date')
    return render(request,'djangoApplication/index.html',{'posts': posts})

def post_detail(request,post_id):
    post = get_object_or_404(Posts,id=post_id)
    context = {'post': post}
    return render(request,'djangoApplication/post_detail.html',context)


@login_required
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request)
        if form.is_valid():
           post = form.save()
           return redirect('home')
    else:
        form=PostForm()
    return render(request,'djangoApplication/add_post.html',{'form':form,'form_title':'Создание поста'})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Posts, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = PostForm(instance=post)

    return render(request, 'djangoApplication/edit_post.html', {'form': form, 'form_title': 'Редактирование поста'})


