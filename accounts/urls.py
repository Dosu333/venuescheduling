from django.urls import path
from . import views
from .views import RegisterView, LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django_registration.backends.activation.views import RegistrationView, ActivationView
from .forms import RegisterForm

app_name = 'accounts'

urlpatterns =[
    path('login/', LoginView.as_view(), name = 'login'),
    path('register/',RegistrationView.as_view(form_class=RegisterForm), name='signup'),
    path('logout/', views.logout, name = 'logout'),
    path('activate/complete',TemplateView.as_view(template_name='django_registration/activation_complete.html'), name = 'activation_complete'),
    path('activate/',ActivationView.as_view(), name = 'django_registration_activate'),
    path('register/complete', TemplateView.as_view(template_name='django_registration/registration_complete'), name = 'registration_complete'),
    path('register/closed', TemplateView.as_view(template_name='django_registration/registration_disallowed.html'), name='registration-disallowed')
]
