from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import render
from django.views.generic import DetailView

from task.forms import (
    PositionForm,
    TaskForm,
    TaskTypeForm,
    WorkerCreationForm,
    WorkerUpdateForm,
)
from task.models import Position, Task, TaskType, Worker


# Create your views here.
@login_required()
def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.all().count()
    num_tasks = Task.objects.all().count()
    num_positions = Position.objects.all().count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
        "num_visits": num_visits + 1,
    }

    return render(request, "home/dashboard.html", context=context)




class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "task_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = (
            Task.objects.select_related("task_type")
            .prefetch_related("assignees", "assignees__position")
            .order_by("is_completed", "deadline", "name")
        )

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:task-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create task"
        context["cancel_url"] = reverse_lazy("task:task-list")
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:task-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update task"
        context["cancel_url"] = reverse_lazy("task:task-list")
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task/confirm_delete.html"
    success_url = reverse_lazy("task:task-list")


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task/task_detail.html"

    def get_queryset(self):
        return Task.objects.select_related("task_type").prefetch_related(
            "assignees",
            "assignees__position",
        )


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "task/worker_list.html"
    context_object_name = "worker_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = Worker.objects.select_related("position").order_by("username")

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(username__icontains=search)

        return queryset


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:worker-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create worker"
        context["cancel_url"] = reverse_lazy("task:worker-list")
        return context


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:worker-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update worker"
        context["cancel_url"] = reverse_lazy("task:worker-list")
        return context


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    template_name = "task/confirm_delete.html"
    success_url = reverse_lazy("task:worker-list")


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    template_name = "task/worker_detail.html"

    def get_queryset(self):
        return Worker.objects.select_related("position").prefetch_related(
            "assignees",
            "assignees__task_type",
        )


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "task/position_list.html"
    context_object_name = "position_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = Position.objects.order_by("name")

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    form_class = PositionForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:position-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create position"
        context["cancel_url"] = reverse_lazy("task:position-list")
        return context


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    form_class = PositionForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:position-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update position"
        context["cancel_url"] = reverse_lazy("task:position-list")
        return context


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    template_name = "task/confirm_delete.html"
    success_url = reverse_lazy("task:position-list")


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task/tasktype_list.html"
    context_object_name = "tasktype_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = TaskType.objects.order_by("name")

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:tasktype-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create task type"
        context["cancel_url"] = reverse_lazy("task:tasktype-list")
        return context


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task/form.html"
    success_url = reverse_lazy("task:tasktype-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update task type"
        context["cancel_url"] = reverse_lazy("task:tasktype-list")
        return context


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    template_name = "task/confirm_delete.html"
    success_url = reverse_lazy("task:tasktype-list")


@login_required
def toggle_assign_to_task(request, pk):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("task:task-detail", args=[pk]))

    worker = Worker.objects.get(id=request.user.id)
    task = Task.objects.get(id=pk)

    if task in worker.assignees.all():
        task.assignees.remove(worker)
    else:
        task.assignees.add(worker)

    return HttpResponseRedirect(reverse_lazy("task:task-detail", args=[pk]))
