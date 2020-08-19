from django.urls import path
from .views import (
    register_view, 
    LoginView,
    LogoutView,
    ProfileDetailView,
    update_profile,
)

app_name = 'accounts'

urlpatterns = [
    path('register/',register_view,name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('profile/<slug:slug>/',ProfileDetailView.as_view(),name="profile"),
    path('profile/update/<slug:slug>/',update_profile,name="profile-update"),
    
]
