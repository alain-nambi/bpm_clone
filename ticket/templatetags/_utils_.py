from django import template
from viewflow.models import Task

register = template.Library()


@register.simple_tag
def get_created_user(process):
    """
    Get the username of the task owner for the initial task in the process.
    """
    task = Task.objects.filter(
        process=process,
        flow_task_type__icontains='START'
    ).select_related('owner').only('owner__username').first()

    return task.owner.username if task and task.owner else "Unknown"
