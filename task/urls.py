from django.urls import path

from task.views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    TaskTypeCreateView,
    TaskTypeDeleteView,
    TaskTypeListView,
    TaskTypeUpdateView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerDetailView,
    WorkerListView,
    WorkerUpdateView,
    PositionCreateView,
    PositionDeleteView,
    PositionListView,
    PositionUpdateView,
    toggle_assign_to_task,
    index,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle-assign/", toggle_assign_to_task, name="toggle-task-assign"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("task-types/", TaskTypeListView.as_view(), name="tasktype-list"),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="tasktype-create"),
    path("task-types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="tasktype-update"),
    path("task-types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="tasktype-delete"),
]

app_name = "task"
