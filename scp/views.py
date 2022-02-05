from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def loginUser(request):
    return render(request, 'registration/login.html')

@login_required
def index(request):
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
def tables(request):
    return render(request, 'tables.html')

@login_required
def typography(request):
    return render(request, 'typography.html')

@login_required
def rtl(request):
    return render(request, 'rtl.html')

@login_required
def upgrade(request):
    return render(request, 'upgrade.html')