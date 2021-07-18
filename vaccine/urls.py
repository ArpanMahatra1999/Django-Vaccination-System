from django.urls import path

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from config.settings import MEDIA_URL, MEDIA_ROOT

from vaccine.views import ListScheduleView, VaccinatedListScheduleView, UnvaccinatedListScheduleView
from vaccine.views import UpdateScheduleView

app_name = 'vaccine'

urlpatterns = [
    path('schedule/list', ListScheduleView.as_view(), name='list-schedule'),
    path('schedule/list/vaccinated', VaccinatedListScheduleView.as_view(), name='vaccinated-list-schedule'),
    path('schedule/list/unvaccinated', UnvaccinatedListScheduleView.as_view(), name='unvaccinated-list-schedule'),
    path('schedule/update/<int:pk>', UpdateScheduleView.as_view(), name='update-schedule'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()