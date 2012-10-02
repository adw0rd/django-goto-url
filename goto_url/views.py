import re
import base64

from django.http import HttpResponseRedirect
from django.views.generic import View


class GotoView(View):
    def dispatch(self, request, url, **kwargs):
        try:
            redirect_url = base64.decodestring(url)
        except (Exception, ), e:
            if e.message == 'Incorrect padding':
                redirect_url = url
                if not re.search(r'^http(s)?://', redirect_url):
                    redirect_url = 'http://{0}'.format(redirect_url)
        return HttpResponseRedirect(redirect_url)
