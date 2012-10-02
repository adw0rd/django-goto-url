from django.template import Library
from goto_url import utils

register = Library()


@register.simple_tag
def goto_url(url):
    return utils.goto_url(url)
