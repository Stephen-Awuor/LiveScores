from django.contrib import admin
from django.urls import path
from . import views
from fixtureviewer import views as fixtureviewer_views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.dashboard, name='dashboard'), 
   path('dashboard/', views.dashboard, name='dashboard'),
   path('teams/', views.season_teams, name='teams'),
]
