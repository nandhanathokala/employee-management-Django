from django.urls import path
from .views import (
    login_view,
    dashboard,
    logout_view,
    profile_view,
    change_password_view
)

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('change-password/', change_password_view, name='change_password'),
    path('logout/', logout_view, name='logout'),
]
