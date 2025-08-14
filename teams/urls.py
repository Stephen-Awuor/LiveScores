from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('current-teams/', views.current_teams, name='current-teams'),
   path('add-team/', views.add_team, name='add-team'),
]