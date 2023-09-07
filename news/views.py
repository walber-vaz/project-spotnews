from django.shortcuts import get_object_or_404, redirect, render

from news.forms import CategoryForm

from .models import News


def home(request):
    news_list = News.objects.all()
    context = {"news_list": news_list}
    return render(request, 'home.html', context)


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    context = {"news": news}
    return render(request, 'news_details.html', context)


def categories_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            return redirect('home-page')
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'categories_form.html', context)
