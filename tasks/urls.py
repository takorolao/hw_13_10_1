from django.urls import path
from .views import get_all_tasks, get_task, delete_task, create_todo_item

urlpatterns = [
    path('tasks/', get_all_tasks, name='get-all-tasks'),
    path('tasks/<int:task_id>/', get_task, name='get-task'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete-task'),
    path('tasks/create/', create_todo_item, name='create-todo-item')
]
