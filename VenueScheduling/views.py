from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class LandingPage(TemplateView):
    template_name = 'land.html'
