from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Custom views
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),

    # Password Management Views
    path('forgot-password/', 
         auth_views.PasswordResetView.as_view(
             template_name='accounts/forgot_password.html', 
             email_template_name='accounts/password_reset_email.html', 
             success_url='/accounts/forgot-password/done/'
         ), 
         name='forgot_password'),
    path('forgot-password/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html', 
             success_url='/accounts/reset/done/'
         ), 
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
    path('change-password/', 
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/change_password.html', 
             success_url='/accounts/change-password/done/'
         ), 
         name='change_password'),
    path('change-password/done/', 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/change_password_done.html'
         ), 
         name='password_change_done'),
]
