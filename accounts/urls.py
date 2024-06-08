from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name = 'signup'),
    path('logout/', views.logout_user, name='logout'),
]