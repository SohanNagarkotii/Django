from django.urls import path
from .views import index,about, create, contactus,partData


urlpatterns = [
    path("",index, name = "home"),
    path("about/", about),
    path("create/", create),
    path("<int:id>/", partData),
    path("contactus/", contactus)
]