# coding=utf-8

from django.conf.urls import url

from . import views

app_name = "compras"

urlpatterns = [
    url(
        r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', views.create_cartitem,
        name='create_cartitem'
    )
]