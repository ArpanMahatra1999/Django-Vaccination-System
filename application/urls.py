from django.urls import path

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from config.settings import MEDIA_URL, MEDIA_ROOT

from application.views import CreateApplicationView

app_name = 'application'

urlpatterns = [
    path('create/<int:pkc>', CreateApplicationView.as_view(), name='create-application'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()