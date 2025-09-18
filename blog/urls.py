from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('manage-news/', views.manage_news, name='manage-news'),
   path('add-news/', views.add_news, name='add-news'),
   path('edit-news/<int:news_id>/edit/', views.news_edit, name='edit-news'),
   path('delete-news/<int:news_id>/edit/', views.news_delete, name='delete-news'),
]