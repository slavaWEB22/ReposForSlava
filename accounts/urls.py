from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('register/',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path("password_reset/",PasswordResetView.as_view(template_name="passwordReset/password_reset_form.html"),name="password_reset"),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name = "passwordReset/password_reset_done.html"),name='password_reset_done'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="passwordReset/password_reset_complete.html"), name='password_reset_complete'),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="passwordReset/password_reset_confirm.html",success_url=reverse_lazy("password_reset_complete")),name='password_reset_confirm'),
    ]
