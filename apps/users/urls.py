from django.urls import path

from apps.books.views import ProfileView
from config.views import register_view, login_view, logout_view

app_name = "users"
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('logout/', logout_view, name='logout'),

]
