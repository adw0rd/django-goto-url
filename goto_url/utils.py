import base64


def goto_url(url):
    """Build link to internal view"""
    url = base64.encodestring(url.encode('utf-8')).replace("\n", "")
    return "/{name}/{url}".format(name="goto", url=url)
