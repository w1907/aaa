from django.urls import path
from authenticate import views

urlpatterns=[
	path('signin', views.signIn, name="signin"),
	path('signout', views.signOut, name="signout"),
	path('signup', views.signUp, name="signup"),
]