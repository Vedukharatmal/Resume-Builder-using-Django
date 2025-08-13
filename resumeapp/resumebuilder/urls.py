from django.urls import path
from django.contrib import admin
from resumebuilder.views import *

urlpatterns = {
    path('', home, name = 'home'),
    path('resume/', gen_resume, name= 'resume'),
    path("admin/", admin.site.urls),
    path("form/", form, name = 'form')
}