from django.urls import path
from .views import register_user, login_user, logout_user, task_list, edit_task, delete_task, dashboard

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tasks', task_list, name='task_list'),  # Default view after login
    path('', dashboard, name='dashboard'),
    path("task/edit/<int:task_id>/", edit_task, name="edit_task"),
    path("task/delete/<int:task_id>/", delete_task, name="delete_task"),
]
