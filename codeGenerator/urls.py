from . import views
from django.urls import path


urlpatterns = [
    path('', views.generate_qr_code, name='generate_qr_code'),
]
