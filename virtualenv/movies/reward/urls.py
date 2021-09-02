from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists', views.artists, name='artists'),
    path('awards', views.awards, name='awards'),
    path('movies', views.movies, name='movies'),
    path('rating', views.rating, name='rating'),
    path('topten/', views.topten, name ='topten'),
    path('leastten/', views.leastten, name ='leastten'),
    path('within/', views.within, name ='within'),
    path('search/', views.search_results, name='search_results'),
    
    ]