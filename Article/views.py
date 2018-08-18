from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from .models import Article
from Channel.models import Channel
from Comment.models import Comment


def get_articles(request, channel_name):
    # TODO
    # page = int(request.GET.get('page', '1'))
    channel = Channel.objects.get(name=channel_name)
    articles = Article.objects.filter(channel=channel, status=1).order_by('-create_ts')
    article_num = len(articles)
    return render_to_response('articles.html', {'articles': articles, 'article_num': article_num})


def get_article(request, article_id):
    # TODO
    # comment_page = int(request.GET.get('comment_page', '1'))
    article_id = int(article_id)
    # TODO 404 error
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article_id, status=1).order_by('create_ts')
    comment_num = len(comments)

    article.views += 1
    article.save()
    return render_to_response('article.html', {'article': article, 'comments': comments, 'comment_num': comment_num})


@login_required
def create_article():
    # TODO
    pass
