from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('invalid',views.invalid,name='invalid'),
    path('logout',views.logout,name='logout'),
    path('passengerinfo',views.passengerinfo,name='passengerinfo'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]