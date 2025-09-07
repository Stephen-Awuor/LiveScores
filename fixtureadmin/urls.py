from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('current-fixtures/', views.currrent_fixtures, name='current-fixtures'),
   path('add-fixture', views.add_fixture, name='add-fixture'),
   path('edit-fixture/<int:fixture_id>/edit/', views.edit_fixture, name='edit-fixture'),
   path('delete-fixture/<int:fixture_id>/edit/', views.delete_fixture, name='delete-fixture'),
]