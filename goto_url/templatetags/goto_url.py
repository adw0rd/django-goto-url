from django.template import Library
from .. import utils

register = Library()


@register.simple_tag
def goto_url(url):
    return utils.goto_url(url)
