from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('submit',views.submit),
    path('show/',views.show)
]