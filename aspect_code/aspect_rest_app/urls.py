from django.urls import path
from django.conf.urls import url
from aspect_rest_app import views


urlpatterns = [
			   path("users/", views.DemoApiView.as_view()),
			   url(r'users/([A-Za-z\-_0-9]+)', views.DemoApiView.as_view()),
			   path("unknown/", views.DemoApiView.as_view()),
			   url(r'unknown/([A-Za-z\-_0-9]+)', views.DemoApiView.as_view()),

			   path("register/", views.RegisterApi.as_view()),

			   path("login/", views.LoginApi.as_view()),


			   
]


