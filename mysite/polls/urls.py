from django.urls import include, path
from . import views
urlpatterns = [
    path('submit', views.IndexView.as_view()), #name='index'),
    path('', views.homepage),
#     path('submit',views.submit),
#     path('show/',views.show)
]


