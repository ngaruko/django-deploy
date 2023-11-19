from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


#class based
class HomeView(TemplateView):
    template_name = 'home/home.html'
    extra_context =  {'date' : datetime.today()}

class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/restricted.html'
    login_url='/admin'

# Create your views here.
# def home(request):
#     return render(request, 'home/home.html', {'date' : datetime.today()})

# @login_required(login_url='/admin')
# def restricted(request):
#     return render(request, 'home/restricted.html', {})