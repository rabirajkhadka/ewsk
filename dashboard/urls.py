from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.home, name="home"),
    path('statistics/', views.statistics_page, name="statistics"),


]
