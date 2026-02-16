from django.urls import path
from . import views

app_name = 'developers'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('regenerate-key/', views.regenerate_api_key, name='regenerate_key'),
]