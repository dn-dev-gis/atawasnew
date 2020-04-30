from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signupuser, name = 'signupuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    path('login/', views.loginuser, name = 'loginuser'),
    path('create/', views.createcontact, name = 'createcontact'),

    path('all/', views.contactall, name = 'contactall')
]
