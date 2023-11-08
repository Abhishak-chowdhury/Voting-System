from myapp.views import *
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('user-dashboard/<slug:user1>',user_home,name='user-dashboard'),
    path('admin-dashboard',admin_home,name='admin-dashboard'),
    path('user-login',user_login,name='user-login'),
    path('user-register',user_register,name='user-register'),
    path('admin-login',admin_login,name='admin-login'),
    path('logout',logout,name='logout'),
    path('admin-logout',Admin_logout,name='admin-logout'),
    path('admin-dashboard/view-voters',view_voters,name='view-voters'),
    path('activate-voter',Activate_Voter,name='activate-voter'),
    path('add-election',Add_Election,name='add-election'),
    path('add-candidate',Add_candidate,name='add-candidate'),
    path('view-candidates',Available_Candidates,name='view-candidates'),
    path('election',User_Election,name='election'),
    path('vote/<str:elec>',vote,name='vote'),
    path('vote-done',Vote_done,name='vote-done'),
    path('search-result',Search_Result,name='search-result'),
    path('view-result/<str:election>',View_Result,name='view-result'),
    path('change-password',Change_password,name='change-password'),
]