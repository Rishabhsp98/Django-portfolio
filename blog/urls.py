from django.contrib import admin
from . import views
from django.urls import include,path
urlpatterns = [
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]
