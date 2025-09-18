from django.contrib import admin
from django.urls import path
from fixtureviewer import views as fixtureviewer_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fixtureviewer.urls')),
    path('', include('accounts.urls')),
    path('', include('fixtureadmin.urls')),
    path('', include('teams.urls')),
    path('', include('blog.urls')),
]
