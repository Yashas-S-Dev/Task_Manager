from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import Task
from .forms import RegisterForm, TaskForm

# Register a user
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

# Login user
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')  # Redirect to task list after login
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# Logout user
def logout_user(request):
    logout(request)
    return redirect('login')

# Task list (dashboard)
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Show only user's tasks

    if request.method == 'POST':  # Handling task creation
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign current user to task
            task.save()
            return redirect('task_list')  # Refresh the page after adding task
    else:
        form = TaskForm()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()  # ✅ Changed 'status' to 'completed'
    pending_tasks = tasks.filter(completed=False).count()  # ✅ Changed 'status' to 'completed'

    priority_counts = {
        'High': tasks.filter(priority='High').count(),
        'Medium': tasks.filter(priority='Medium').count(),
        'Low': tasks.filter(priority='Low').count(),
    }

    return render(request, 'tasks/dashboard.html', {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'priority_counts': priority_counts,
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")  # Redirect back to task list
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {"form": form, "task": task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/delete_task.html", {"task": task})

