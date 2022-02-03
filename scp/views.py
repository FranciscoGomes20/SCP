from django.shortcuts import render

# Create your views here.
def loginUser(request):
    return render(request, 'registration/login.html')

def index(request):
    return render(request, 'dashboard.html')