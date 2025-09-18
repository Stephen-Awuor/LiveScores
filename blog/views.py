from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm
from django.contrib import messages

@login_required
def manage_news(request):
    news_list = News.objects.order_by('-created_at')
    return render(request, 'admin/manage_news.html', {'news_list': news_list})

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'News successfully added')
            return redirect('manage-news')
    else:
        form = NewsForm()
    return render(request, 'admin/add_news.html', {'form': form})

@login_required
def news_edit(request, news_id):
    news_obj = get_object_or_404(News, pk=news_id)
    form = NewsForm(request.POST or None, instance=news_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Changes successfully saved')
        return redirect('manage-news') 
    return render(request, 'admin/edit_news.html', {'form': form, 'news_obj': news_obj})

@login_required
def news_delete(request, news_id):
    news_obj = get_object_or_404(News, pk=news_id)
    if request.method == "POST":
        news_obj.delete()
        return redirect('manage-news') 
    return render(request, 'admin/confirm_delete_news.html', {'news_obj': news_obj})
