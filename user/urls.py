from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from config.settings import MEDIA_URL, MEDIA_ROOT

from user.views import *

app_name = 'user'

urlpatterns = [
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()