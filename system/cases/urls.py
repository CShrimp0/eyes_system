from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('case_select/', views.case_select, name='case_select'),
    path('', views.index, name='index'),
]