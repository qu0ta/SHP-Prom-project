from .models import News


def get_last_news(count: int) -> list[News]:
    return get_all_news()[:count]


def get_all_news() -> list[News]:
    return News.objects.all().order_by('-created_at')
