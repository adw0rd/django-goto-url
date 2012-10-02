django-goto-url
========================

Wraps external links in base64 and relocate on the special View, later redirect to source URL

    pip install django-goto-url

For more details see:
------------------------

* http://github.com/adw0rd/django-goto-url - the GitHub repository
* http://pypi.python.org/pypi/django-goto-url - the PyPI page


Settings:
------------------------

Add to ``settings.py``::

    INSTALLED_APPS = (
        'goto_url',
    )

Add to ``url.py``::

    urlpatterns = patterns('',
        url(r'', include('goto_url.urls')),
    )


Using:
------------------------

1. The templates can be used as follows::

    {% load goto_url %}
    {% goto_url comment.user_url %}
    {% goto_url "http://adw0rd.com/" %}

2. Not in the templates can be used as follows::

    from goto_url.utils import goto_url
    
    goto_url('http://adw0rd.com/')
    >>> '/goto/aHR0cDovL2FkdzByZC5jb20v'
