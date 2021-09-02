from os import name
from doc_manage.models import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url 
from django.views.static import serve


urlpatterns = [
    # path('', views.home, name= 'home'),
    path('',views.index, name="index"),
    # path('upload/', views.upload_file, name="upload"),
    # path('report/', views.report_data, name='report'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('upload',views.upload, name='upload'),
    path('report',views.report, name='report')
    # url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
