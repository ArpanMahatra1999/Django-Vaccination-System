from django.urls import path

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from config.settings import MEDIA_URL, MEDIA_ROOT

from child.views import CreateChildView, ListChildView, UpdateChildView, DeleteChildView, DetailChildView

app_name = 'child'

urlpatterns = [
    path('create', CreateChildView.as_view(), name='create-child'),
    path('list', ListChildView.as_view(), name='list-child'),
    path('update/<int:pk>', UpdateChildView.as_view(), name='update-child'),
    path('delete/<int:pk>', DeleteChildView.as_view(), name='delete-child'),
    path('detail/<int:pk>', DetailChildView.as_view(), name='detail-child')
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()