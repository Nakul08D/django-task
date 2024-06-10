from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signdetail, name='signin'),
    path('login/', views.logindetail, name='login'),
    path('addbook/', views.addbook, name='addbook'),
    path('deletebook/<int:id>/', views.deletebook, name='deletebook'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('admin-booklist/', views.admin_booklist, name='admin-booklist'),
    path('user/booklist/', views.user_booklist, name='user/booklist'),
    path('logout/', views.logout_user, name='logout')
    
]
