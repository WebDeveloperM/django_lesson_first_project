from django.urls import path

from post.views import article_func

urlpatterns = [
    path('', article_func)
]