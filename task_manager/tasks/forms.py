from django import forms
from django.contrib.auth.models import User
from .models import Task, Category

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    # Allow users to enter a new category while creating a task
    new_category = forms.CharField(
        max_length=100,
        required=False,
        label="New Category"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'completed', 'categories']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        task = super().save(commit=False)

        if commit:
            task.save()  # ✅ Ensure task gets an ID

        return task  # ❌ Do NOT modify ManyToMany here! Handle it in views.py



