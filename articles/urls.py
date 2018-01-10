from django.urls import path
# from django.contrib import admin
from .import views 


app_name = 'articles'

urlpatterns = [
	path('', views.article_list, name='list'),
	path('create', views.article_create, name='create'),
	path('<slug:slug>/', views.detail , name='detail')
]