from django.contrib import admin

from .models import Categories, News, Users

admin.site.register(Categories)
admin.site.register(News)
admin.site.register(Users)
