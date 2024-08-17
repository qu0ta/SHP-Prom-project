from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def media(path):
    print(path)
    return (settings.MEDIA_ROOT + path)
