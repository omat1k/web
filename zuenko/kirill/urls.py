from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_view, name='info'),
    path('group/', views.group_view, name='group'),
    path('age/', views.age_view, name='age'),
    path('', views.home_view, name='home'),
]