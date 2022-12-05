from .models import Task
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["number", "title", "task", "prim"]
        widgets = {"number": NumberInput(attrs={'class': 'form-control',
                                            'placeholder' : 'Введите номер'}),
                   "title": TextInput(attrs={'class':'form-control',
                                            'placeholder' : 'Введите название'}),
                   "task": Textarea(attrs={'class': 'form-control',
                                             'placeholder' : 'Введите описание'}),
                   "prim": TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Введите примечание'}),
                   }