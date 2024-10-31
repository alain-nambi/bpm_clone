import time
from os import times

from django.template.defaultfilters import title
from viewflow import flow
from viewflow.base import this, Flow

from .models import HelpDeskProcess
from .views import StartHelpDeskView


class HelpDeskFlow(Flow):
    process_class = HelpDeskProcess
    process_title = 'HelpDesk'
    process_description = (
        'This workflow is used to request help from Helpdesk'
    )

    start = flow.Start(
        StartHelpDeskView,
        task_title="Start request"
    ).Next(this.delay)

    delay = flow.Handler(
        this._handle_delay
    ).Next(this.end)

    end = flow.End()

    def _handle_delay(self, activation):
        print("Starting delay for 1 minute...")
        time.sleep(10)
        print("Delay ended. Proceeding to end of the flow.")