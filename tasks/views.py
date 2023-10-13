from django.shortcuts import render
from django.http import JsonResponse
from .models import TodoItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def get_all_tasks(request): # для получения задач всех задач
    tasks = TodoItem.objects.all()
    data = [{'id': task.id, 'title': task.title, 'description': task.description, 'created_at': task.created_at} for task in tasks]
    return JsonResponse(data, safe=False)


def get_task(request, task_id): # для одной задачи
    task = get_object_or_404(TodoItem, id=task_id)
    data = {'id': task.id, 'title': task.title, 'description': task.description, 'created_at': task.created_at}
    return JsonResponse(data)

def delete_task(request, task_id): # для удаления
    task = get_object_or_404(TodoItem, id=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully'})

def create_todo_item(request):
    new_task = TodoItem(title="Название задачи", description="Описание задачи")
    new_task.save()
    return HttpResponse("Новая задача создана успешно!")
