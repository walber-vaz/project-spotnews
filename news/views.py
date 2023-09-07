from django.shortcuts import get_object_or_404, redirect, render

from news.forms import CategoryForm, NewsForm

from .models import Categories, News


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


def news_form(request):
    categories = Categories.objects.all()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # Crie uma instância de News com base nos dados do formulário
            news = News(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author_id=form.cleaned_data['author'].id,
                created_at=form.cleaned_data['created_at'],
                image=form.cleaned_data['image'],
            )
            news.save()

            # Associe as categorias selecionadas à notícia
            selected_categories = form.cleaned_data['categories']
            news.categories.set(selected_categories)

            # Redirecione para a página principal após o envio do formulário
            return redirect('home-page')
    else:
        form = NewsForm()

    context = {
        'form': form,
        'categories': categories,
    }

    return render(request, 'news_form.html', context)
