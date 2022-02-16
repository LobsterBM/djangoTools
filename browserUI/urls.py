from django.urls import path , include , re_path

from . import views
urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('<moduleID>', views.moduleConfig, name='config'),
]