from django.contrib import admin
from django.urls import path
from . import views
from fixtureviewer import views as fixtureviewer_views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.dashboard, name='dashboard'), 
   path('dashboard/', views.dashboard, name='dashboard'),
   path('previous/', views.previous_matches, name='previous'),
   path('upcoming/', views.upcoming_matches, name='upcoming'),
    path('teams/', views.season_teams, name='teams'),
]
