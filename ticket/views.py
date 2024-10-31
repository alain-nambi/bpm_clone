from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from viewflow.flow.views import get_next_task_url, StartFlowMixin, DetailProcessView, ProcessListView
from django.contrib import messages

from .forms import HelpDeskForm
from .models import Ticket


class StartHelpDeskView(StartFlowMixin, generic.FormView):
    """View to start a ticket in helpdeskprocess"""
    form_class = HelpDeskForm

    def get_context_data(self, **kwargs):
        context = super(StartHelpDeskView, self).get_context_data(**kwargs)
        context['new_process'] = 'New Ticket'
        context['current_process'] = 'Ticket'
        context['bar_name'] = 'Helpdesk'
        return context

    def get_form_kwargs(self):
        kwargs = super(StartHelpDeskView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        title = form.cleaned_data['title']
        contact = form.cleaned_data['contact']
        details = form.cleaned_data['details']
        ticket = Ticket.objects.create(
            title=title,
            details=details,
            contact=contact,
            )
        self.activation.process.ticket = ticket
        self.activation.done()

        return redirect(
            get_next_task_url(
                self.request,
                self.activation.process
                )
            )


class ProcessDetailView(DetailProcessView):
    context_object_name = 'process'
    pk_url_kwarg = 'process_pk'

    def get_context_data(self, **kwargs):
        context = super(ProcessDetailView, self).get_context_data(**kwargs)
        process = context['process']
        ticket = process.ticket
        context["task_list"] = process.task_set.object.order_by("created")

        context['data'] = [
            ('Title', ticket.title),
            ('Contact', ticket.contact)
        ]


        context['textareas'] = [
            ('Details', ticket.details)
        ]

        context['new_process'] = 'New Ticket'
        return context


class ListProcessView(ProcessListView):
    """View to list all ticket's process"""
    def get_context_data(self, **kwargs):
        context = super(ListProcessView, self).get_context_data(**kwargs)
        context['flow_class'] = self.flow_class
        context['test_data'] = 'Hello Flow'
        return context

    def get_queryset(self):
        """Filtered process list."""
        process = self.flow_class.process_class.objects.filter(
                    flow_class=self.flow_class
        ).order_by('-created')

        process = [i for i in process if i.created_by == self.request.user]

        return process