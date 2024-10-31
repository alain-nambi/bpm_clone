#!/usr/bin/env python
# encoding: utf-8


from django.urls import include, path
from viewflow.flow.viewset import FlowViewSet
from .flows import HelpDeskFlow
from .models import HelpDeskProcess
from .views import ProcessDetailView, ListProcessView

app_name = "ticket"

nodes = [i.name for i in HelpDeskFlow._meta.nodes()]

"""
nodes_urls = [
    path('<int:process_pk>/{}/<int:task_pk>/detail/'.format(i.name),
        MyDetailTaskView.as_view(),
        name='{}__detail'.format(i.name),
        kwargs={'flow_task': i}
        )
    for i in HelpDeskFlow._meta.nodes()
    ]
"""

urlpatterns = [
    path(
        'helpdesk/',
        include((FlowViewSet(HelpDeskFlow).urls, "ticket"), namespace='helpdesk'),
        kwargs={'flow_class': HelpDeskFlow}
    ),

    path('',
         ListProcessView.as_view(),
         name='index'
    ),

    path('<int:process_pk>/',
        ProcessDetailView.as_view(),
        name='detail'
    ),
]
