from .models import News, User, Comment


def get_last_news(count: int) -> list[News]:
    return get_all_news()[:count]


def get_all_news() -> list[News]:
    return News.objects.all().order_by('-created_at')


def get_news(news_id: int) -> News:
    try:
        return News.objects.get(pk=news_id)
    except News.DoesNotExist:
        return None

def get_user_by_user_id(user_id: int) -> User:
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None


def create_comment(author: User, news: News, text: str, created_at=None) -> None:
    if created_at:
        Comment(author=author, news=news, text=text, created_at=created_at).save()
        return
    Comment(author=author, news=news, text=text).save()

def get_comments_by_news_id(news_id: int) -> list[Comment]:
    return Comment.objects.filter(news=News.objects.get(pk=news_id))