from django.shortcuts import render, redirect
# Create your views here.
from .forms import TaskForm
from .models import Task

# Create your views here.


def home(request):
    task_list = Task.objects.all()
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'home.html', {'form': form, 'task_list': task_list})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
