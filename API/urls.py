from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/table$', views.tables_list),
    url(r'^api/table/(?P<pk>[0-9]+)$', views.table_detail),
]
