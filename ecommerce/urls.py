from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('contato/', views.contact, name='contato'),
    url(r'^entrar/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^sair/$', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    url(r'^catalogo/', include('catalogo.urls', namespace='catalog')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]
