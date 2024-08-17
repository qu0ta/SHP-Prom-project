from .models import News


def get_last_news(count: int) -> list[News]:
    return get_all_news()[:count]


def get_all_news() -> list[News]:
    return News.objects.all().order_by('-created_at')


def get_news(news_id: int) -> News:
    try:
        return News.objects.get(pk=news_id)
    except News.DoesNotExist:
        return None
