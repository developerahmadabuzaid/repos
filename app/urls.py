from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news_list', views.news_list, name='news_list'),
    path('about_view', views.about_view, name='about_view'),
    path('contact_view', views.contact_view, name='contact_view'),
]