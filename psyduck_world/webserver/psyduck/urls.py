from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('validate', views.validate),
    path('validate_get_state', views.validate_get_state),
    path('login', views.login),
    path('login_get_state', views.login_get_state),
    path('login_get_qrcode', views.login_get_qrcode),
    path('login_verify_get', views.login_verify_get),
    path('login_verify_set', views.login_verify_set),
]