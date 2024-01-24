from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "blog/login.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # creating the new user .
        new_user = User.objects.create_user(username=name, email= email, password=password)
        new_user.save()
        return redirect('/login')
    return render(request, "blog/signup.html")

def login_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None :
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/login')

    return render(request, "blog/login.html")

def home(request):

    posts = Posts.objects.all()
    print(posts)
    context = {
        'posts': posts
    }

    return render(request, "blog/home.html", context)

def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_post = Posts(title=title, content=content, author=request.user)
        new_post.save()
        return redirect("/home")
    else:
        return render(request, 'blog/new_post.html')

def my_post(request):
    pass

