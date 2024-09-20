from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products', views.Products_List.as_view(), name='products'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('about', views.About.as_view(), name='about'),
    path('contact', contact, name='contact'),
]
