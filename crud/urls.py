from django.urls import path
from .views import index,about, create, contact,partData,deleteBlog,updateBlog,signIn,signUp,logOut,post

app_name = "crud"
urlpatterns = [
    path("",index, name = "home"),
    path("about.html/", about, name = "about"),
    path("index.html/", post, name = "post"),
    path("create.html/", create, name = "create"),
    path("signIn.html/", signIn, name = "signIn"),
    path("signUp.html/", signUp, name = "signUp"),
    path("logOut.html/", logOut, name = "logOut"),
    path("<int:id>/", partData, name = "particular"),
    path("contact.html/", contact, name = "contactus"),
    path("delete/<int:id>/", deleteBlog, name = "deleteblog"),
    path("update/<int:id>/", updateBlog, name = "updateblog")
]