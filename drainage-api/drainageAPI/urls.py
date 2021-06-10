from django.contrib import admin
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from webapp import views
urlpatterns = [
    re_path(r'^$', views.homePage),
    re_path(r'^data/$', views.dataPage),
    path('admin/', admin.site.urls),
    path('api/dataset/', views.dataSetList.as_view()),
    path('api/station/', views.stationList.as_view()),
    re_path(r'api/datasetstation/(?P<stationID>[\w-]+)/$',
            views.dataSetStation.as_view()),
    re_path(r'api/trend/(?P<stationID>[\w-]+)/$',
            views.trendList.as_view()),
    re_path(r'api/average/(?P<stationID>[\w-]+)/$',
            views.averageList.as_view()),
    re_path(r'api/stationNumber/(?P<stationID>[\w-]+)/$',
            views.stationNumber.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
