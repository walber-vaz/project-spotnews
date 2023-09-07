from django.urls import path

from news.views import categories_form, home, news_details

urlpatterns = [
    path("categories/", categories_form, name='categories-form'),
    path("", home, name="home-page"),
    path("<int:id>/", news_details, name="news-details-page"),
]
