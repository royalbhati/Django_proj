from django.urls import path
from . import views


urlpatterns=[ 
			  path('',views.HomePage.as_view(),name='a'),
			  path('about',views.About.as_view(),name='c'),	

]

