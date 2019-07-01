"""Blog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from User_Registration_App import views as user_reg_app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog_App.urls', namespace="Blog_App")),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # what is next_page?
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout', kwargs={'next_page':'/'}),
    path('accounts/register', user_reg_app_views.user_registration, name='register'),
    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password-reset.html'), name='password-reset'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view()),
    ]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
