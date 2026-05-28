from django import forms
from django.contrib.auth.forms import UserCreationForm

from task.models import Position, Task, TaskType, Worker


class PositionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    class Meta:
        model = Position
        fields = ("name",)


class TaskTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    class Meta:
        model = TaskType
        fields = ("name",)


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S"],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == "is_completed":
                field.widget.attrs.setdefault("class", "form-check-input")
                continue

            default_class = "form-control"
            if getattr(field.widget, "allow_multiple_selected", False):
                default_class = "form-select"
            if field.widget.__class__.__name__ in {"Select", "SelectMultiple"}:
                default_class = "form-select"

            field.widget.attrs.setdefault("class", default_class)

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "is_completed",
            "priority",
            "task_type",
            "assignees",
        )
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "assignees": forms.SelectMultiple(attrs={"size": 8}),
        }


class WorkerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "position":
                field.widget.attrs.setdefault("class", "form-select")
            else:
                field.widget.attrs.setdefault("class", "form-control")

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        )


class WorkerUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "position":
                field.widget.attrs.setdefault("class", "form-select")
            else:
                field.widget.attrs.setdefault("class", "form-control")

    class Meta:
        model = Worker
        fields = ("first_name", "last_name", "email", "position")
