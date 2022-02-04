from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def loginUser(request):
    return render(request, 'registration/login.html')

@login_required
def index(request):
    return render(request, 'dashboard.html')