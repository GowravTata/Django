from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Using include, we can pass a string that calls all the urls of the challenges are included
    path("challenges/",include("challenges.urls")),
]
