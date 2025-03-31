from rest_framework import serializers
from .models import Task, Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # ✅ Exposes all fields in the Task model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # ✅ Exposes all fields in the Category model
