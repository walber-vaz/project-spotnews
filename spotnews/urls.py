from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from news_rest.views.categories_view import CategoriesViewSet
from news_rest.views.news_view import NewsViewSet
from news_rest.views.users_view import UsersViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoriesViewSet)
router.register(r"users", UsersViewSet)
router.register("news", NewsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("news.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
