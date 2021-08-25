from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('submit', views.artis,name='submit'),
    path('submitt', views.awards),
    path('submittt', views.movie),
    path('submitttt', views.rates),
]