
from django.urls import path
from base_app import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'base_app'

urlpatterns = [
    path("",views.renderHome,name="home"), 
    path("index/",views.renderIndex,name="index"), 
    path('dashboard/', views.dashboard, name='dashboard'),
] 
