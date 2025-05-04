from django.shortcuts import render
from .models import Article, Category
from django.shortcuts import render, get_object_or_404

def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()  # <-- add this line
    return render(request, 'home.html', {'articles': articles, 'categories': categories})


def category_articles(request, category_id):
    categories = Category.objects.all()
    selected_category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category=selected_category).order_by('-created_at')
    return render(request, 'category_articles.html', {'categories': categories, 'articles': articles, 'selected_category': selected_category})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})