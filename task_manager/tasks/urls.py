#tasks/urls.py
from django.urls import path
from .views import register_user, login_user, logout_user, task_list, edit_task, delete_task, dashboard, delete_category, TaskListCreateView, TaskRetrieveUpdateDeleteView, CategoryListCreateView, CategoryRetrieveUpdateDeleteView

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tasks', task_list, name='task_list'),  # Default view after login
    path('', dashboard, name='dashboard'),
    path("task/edit/<int:task_id>/", edit_task, name="edit_task"),
    path("task/delete/<int:task_id>/", delete_task, name="delete_task"),
    path('delete-category/<int:category_id>/', delete_category, name='delete-category'), 
    # ✅ Task API Endpoints
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
    # ✅ Category API Endpoints
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),
]
