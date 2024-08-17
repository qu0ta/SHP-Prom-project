from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def media(path):
    return (settings.MEDIA_ROOT + path)
