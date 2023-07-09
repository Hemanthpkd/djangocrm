from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.Logout_user,name='logout'),
    path('register/',views.Register_user,name='register'),
    path('records/<int:id>',views.Customer_record,name='record'),
    path('delete_record/<int:id>',views.Delete_record,name='delete_record'),
    path('add_record/',views.Add_record,name='add_record'),
    path('update_record/<int:id>',views.Update_record,name='update_record'),
]

