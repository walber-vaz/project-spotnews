from django.urls import path

from news.views import categories_form, home, news_details, news_form

urlpatterns = [
    path("", home, name="home-page"),
    path("news/", news_form, name="news-form"),
    path("news/<int:id>/", news_details, name="news-details-page"),
    path("categories/", categories_form, name='categories-form'),
]
