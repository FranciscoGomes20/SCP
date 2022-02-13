from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *

# Create your views here.
def loginUser(request):
    return render(request, 'registration/login.html')

@login_required
def index(request):
    return render(request, 'home.html', {'chamados': Chamado.objects.all()})

@login_required
def register_tickets(request):
    return render(request, 'register-tickets.html')

@login_required
def all_tickets(request):
    return render(request, 'all-tickets.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def icons(request):
    return render(request, 'icons.html')

@login_required
def map(request):
    return render(request, 'map.html')

@login_required
def notifications(request):
    return render(request, 'notifications.html')

@login_required
def user(request):
    return render(request, 'user.html')

@login_required
def typography(request):
    return render(request, 'typography.html')

    