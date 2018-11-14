from django.urls import path
from checklist import views

urlpatterns=[
	path('checklist', views.checkList, name="checklist"),
]