from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$',views.register.as_view()),
	url(r'^logout/$',views.logoff.as_view()),
]