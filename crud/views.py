from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import Blog, Contactus
from .forms import Blogfroms

# Create your views here.
# def index(request):
#     blog = Blog.objects.all()
#     return render(request, "crud/home.html", {"blogs": blog})

def index(request):
    return render(request, "crud/home.html")

def post(request):
    return render(request, "crud/index.html")

def about(request):
    return render(request, "crud/about.html")

def create(request):
    form = Blogfroms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "crud/create.html", {"form": form})


def partData(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog":blog
    }
    return render(request, "crud/index.html",context)


def contactus(request):
    if(request.method == "POST"):
        dataName = request.POST.get("name")
        dataEmail = request.POST.get("email")
        
        contactus = Contactus(
            name=dataName,
            email=dataEmail
        )
        contactus.save()

    return render(request, "crud/contactus.html")

def deleteBlog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("home")

def signUp(request):
    return request

def signIn(request):
    return request

def logOut(request):
    return request

def contact(request):
    return render(request, "crud/contact.html")

def updateBlog(request, id):
    blog = Blog.objects.get(id=id)
    form = Blogfroms(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "crud/create.html", {"form": form})
