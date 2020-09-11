from django.shortcuts import render, redirect
# Create your views here.
from .forms import TaskForm
from .models import Task

# Create your views here.


def home(request):
    task_list = Task.objects.all()
    task_form = TaskForm(request.POST)
    if task_form.is_valid():
        task_form.save()
        return redirect('home')
    else:
        task_form = TaskForm()
    return render(request, 'home.html', {'task_list': task_list, 'task_form': task_form})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
