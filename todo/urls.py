from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('signed_up', views.signed_up, name = 'signed_up'),
    path('logged_in', views.logged_in, name = 'logged_in'),
    path('dashboard/<int:user_id>', views.dashboard, name = 'dashboard'),
    path('dashboard/add/<int:user_id>', views.add_task, name = 'add_task'),
    path('dashboard/remove/<int:user_id>', views.remove_task, name = 'remove_task'),
    path('signup/failed', views.signup_failed, name = 'signup_failed'),
]
