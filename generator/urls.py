from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_home'),
    path('about', views.about, name='app_about'),
    path('code', views.codeurl, name='app_code'),
    path('more', views.more, name='app_more'),
]