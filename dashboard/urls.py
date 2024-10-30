from django.conf import settings
from django.urls import include, path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index_view)
]