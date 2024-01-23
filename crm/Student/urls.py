from django.contrib import admin
from django.urls import path,include 
#from customer.views import CustomerListing
from Student import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


admin.site.site_header="CRM TOOL"
admin.site.site_title="Welcome CRM"



urlpatterns = [
	path('',views.home,name="index"),

    path('login/',views.login,name = 'login'),
    path('logout',views.logout, name="logout"),


	#path('index',views.index, name="index"),
	#path('signup',views.signup, name="signup"),
	
	#path('register',views.register_view, name="register_url"),
	

    #path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    #path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='reset_password_done'),

    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='reset_password_confirm'),

    #path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='reset_password_complete'),





  
]