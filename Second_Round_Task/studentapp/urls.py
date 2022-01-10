from django.urls import path
from . import views
from django.contrib.auth import views as auth_view    

urlpatterns = [
    path('',views.base_index),
    path('search/',views.search_name,name='search'),
    path('index/',views.index,name='index'),
    path('login/',auth_view.LoginView.as_view(template_name='studentapp/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name='signup'),
    path('changepwd/',views.change_password,name='changepwd'),

    path('create/',views.create_student_details,name='create'),
    path('display/<int:id>/',views.display_student_details,name='display'),
    path('update/<int:id>/',views.update_student_details,name='update'),
    path('delete/<int:id>/',views.delete_student_details,name='delete'),






]