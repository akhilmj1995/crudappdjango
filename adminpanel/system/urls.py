from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('', views.home, name='home'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.user_signup, name='signup'),
    path('panel/',views.adminpage,name='adminpage'),
    path('createuser/',views.createuser,name='create'),
    path('delete/<pk>', views.delete, name='delete'),
    path('edit/<pk>',views.edit,name='edit'),
]