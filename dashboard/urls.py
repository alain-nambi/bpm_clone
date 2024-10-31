from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views


app_name = 'dashboard'

ticket_urls = [
    path('ticket/', include('ticket.urls'))
]


urlpatterns = [
    path('', login_required(views.index_view), name='index'),
    path('login/',
         auth_views.LoginView.as_view(template_name="login.html"),
         name='login'
    ),
    path('logout/',
        auth_views.LogoutView.as_view(
            next_page='dashboard:login'
        ),
        name='logout'
    ),
] + ticket_urls