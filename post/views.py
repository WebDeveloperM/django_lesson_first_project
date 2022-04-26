from django.shortcuts import render
from .models import Article

# Create your views here.

def article_func(request):
    articles = Article.objects.all()
    return render(request, 'articles_list.html', {'maqolalar': articles})
