#views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import Task, Category
from .forms import RegisterForm, TaskForm
from rest_framework import generics
from .serializers import TaskSerializer, CategorySerializer

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
    tasks = Task.objects.filter(user=request.user)  # Get only the user's tasks
    categories = Category.objects.all()  # Get all categories
    # Get filters
    category_id = request.GET.get("category")
    status_filter = request.GET.get("status")
    search_query = request.GET.get("search")
    # Apply category filter
    if category_id:
        tasks = tasks.filter(categories__id=category_id)
    # Apply status filter
    if status_filter == "completed":
        tasks = tasks.filter(completed=True)
    elif status_filter == "pending":
        tasks = tasks.filter(completed=False)
    # Apply search filter (case-insensitive search)
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Create task (not saved yet)
            task.user = request.user
            task.save()  # Save task (assigns ID)
            # Handle ManyToMany relationships safely
            if "categories" in form.cleaned_data:
                selected_categories = form.cleaned_data["categories"]
                task.categories.set(selected_categories)

            # Handle new category creation
            new_category_name = form.cleaned_data.get("new_category")
            if new_category_name:
                category, created = Category.objects.get_or_create(name=new_category_name)
                task.categories.add(category)
            return redirect("task_list")
        else:
            print(form.errors)  # Debugging line to see form validation errors
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks, "categories": categories, "form": form},
    )

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)  # Show only user’s categories

    return render(request, 'tasks/dashboard.html', {
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(completed=True).count(),
        'pending_tasks': tasks.filter(completed=False).count(),
        'categories': categories,  # Send categories to the template
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    categories = Category.objects.all()  # Fetch all categories
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)
            updated_task.save()
            # ✅ Handle ManyToMany relationships (categories)
            if "categories" in form.cleaned_data:
                selected_categories = form.cleaned_data["categories"]
                updated_task.categories.set(selected_categories)  # ✅ Update categories properly
            # ✅ Handle new category creation
            new_category_name = form.cleaned_data.get("new_category")
            if new_category_name:
                category, created = Category.objects.get_or_create(name=new_category_name)
                updated_task.categories.add(category)
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form, "categories": categories, "task": task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/delete_task.html", {"task": task})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Category.objects.get_or_create(name=name)  # Avoid duplicates
    return redirect("task_list")

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    category.delete()
    return redirect('dashboard')  # Redirect to dashboard after deletion

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# ✅ Category API
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer