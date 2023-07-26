from django.urls import path
from .views import index,about, create, contactus,partData,deleteBlog,updateBlog


urlpatterns = [
    path("",index, name = "home"),
    path("about/", about),
    path("create/", create),
    path("<int:id>/", partData, name = "particular"),
    path("contactus/", contactus),
    path("delete/<int:id>/", deleteBlog, name = "deleteblog"),
    path("update/<int:id>/", updateBlog, name = "updateblog")
]