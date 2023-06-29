from django.forms import ModelForm
from .models import TodoModel


class CreateTodoModelForm(ModelForm):
    class Meta:
        model = TodoModel
        exclude = ['task_status', 'created_at']
