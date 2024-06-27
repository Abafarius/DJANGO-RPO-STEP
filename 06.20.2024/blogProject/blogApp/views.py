from django.shortcuts import render, redirect

# Create your views here.
from .forms import ArticleForm

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_success')
    else:
        form = ArticleForm()
    return render(request, 'blog/create_article.html', {'form': form})

def article_success(request):
    return render(request, 'blog/article_success.html')
