from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'
