from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from teams.models import Teams
from blog.models import News
from fixtureadmin.models import Fixture

# Create your views here.

def dashboard(request):
    fixtures = Fixture.objects.all().order_by('-match_date')
    return render(request, 'viewer/livescore.html', {'fixtures': fixtures})

def season_teams(request):
    teams = Teams.objects.all()
    return render(request, 'viewer/teams.html' , {'teams': teams})

def latest_news(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'viewer/blog_list.html' , {'news': news})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'viewer/blog.html' , {'news': news})


