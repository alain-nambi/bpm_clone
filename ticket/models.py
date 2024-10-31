from django.db import models
from datetime import datetime
from viewflow.models import Process


class Ticket(models.Model):
    start_date = models.DateTimeField(
        default=datetime.now()
    )

    end_date = models.DateTimeField(
        default=datetime.now()
    )

    title = models.CharField(
        max_length=150
    )

    details = models.TextField(
        blank=True,
        null=True
    )

    contact = models.CharField(
        max_length=150,
        null=True
    )

class HelpDeskProcess(Process):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='helpdesk'
    )