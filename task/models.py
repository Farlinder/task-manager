from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="worker")

    def __str__(self):
        return f"{self.username} ({self.position.name})"


class Task(models.Model):
    """Task model."""

    class Priority(models.TextChoices):
        URGENT = "URGENT", "Urgent"
        HIGH = "HIGH", "High"
        MEDIUM = "MEDIUM", "Medium"
        LOW = "LOW", "Low"

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=Priority.choices, default=Priority.MEDIUM, max_length=6)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="task")
    assignees = models.ManyToManyField(Worker, related_name="assignees")

    def __str__(self):
        return self.name
