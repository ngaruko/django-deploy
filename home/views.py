from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/home.html', {'date' : datetime.today()})

@login_required(login_url='/admin')
def restricted(request):
    return render(request, 'home/restricted.html', {})