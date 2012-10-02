from django.conf.urls import patterns, url

from views import GotoView

urlpatterns = patterns(
    '',
    url(r'^goto/(.+)$', GotoView.as_view()),
)
