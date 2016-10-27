from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.Home.as_view(),name="Home"),
	url(r'^perfil/',views.Perfil.as_view(),name="Perfil"),
]