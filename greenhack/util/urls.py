from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload_products, name='upload_products'),
]