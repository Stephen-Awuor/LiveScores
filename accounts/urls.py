from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   # Auth
   path('admin-login/', views.admin_login, name='admin-login'),
   path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
   path('logout/', views.admin_logout, name='logout'),
]
