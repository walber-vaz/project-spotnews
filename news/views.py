from django.shortcuts import get_object_or_404, render

from .models import News


def home(request):
    news_list = News.objects.all()
    context = {"news_list": news_list}
    return render(request, 'home.html', context)


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    context = {"news": news}
    return render(request, 'news_details.html', context)
