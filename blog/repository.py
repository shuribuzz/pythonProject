from blog.models import Article, Comment


def get_all_articles():
    articles = Article.objects.all()
    return articles


def get_all_comments():
    comments = Comment.objects.all()
    return comments
