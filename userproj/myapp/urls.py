from django.urls import path
from .import views

urlpatterns=[path("",views.signup,name="signup"),
path("home/",views.home,name="home"),
path("logout/",views.logout,name="logout"),
path("login/",views.login,name="login"),




]