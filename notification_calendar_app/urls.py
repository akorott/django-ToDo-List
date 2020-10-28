from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('registration/', views.registration, name='registration'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update_task/<str:pk>/', views.UpdateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ="notification_calendar_app/password_reset.html"), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="notification_calendar_app/password_reset_sent.html"), name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name ="notification_calendar_app/password_reset_form.html"), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name ="notification_calendar_app/password_reset_done.html"), name='password_reset_complete'),

]

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
