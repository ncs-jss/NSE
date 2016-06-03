from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index.as_view(),name = 'index'),
	url(r'^sell/$',views.sell.as_view(),name = 'sell'),
	url(r'^buy/$',views.buy.as_view(),name = 'buy'),
	url(r'^leader/$',views.leaderboard.as_view(),name = 'leaderboard'),
	
]