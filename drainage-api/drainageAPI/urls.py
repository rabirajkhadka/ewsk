from django.contrib import admin
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
urlpatterns = [
    re_path(r'', views.webPages.homepage),
    path('admin/', admin.site.urls),
    path('average/', views.averageList.as_view()),
]
