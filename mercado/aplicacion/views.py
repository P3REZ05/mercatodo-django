from django.shortcuts import render

def administrador(request):
    return render(request, 'dashboardadmin.html')

def base(request):
    return render(request, 'base.html')

def rembolso(request):
    return render(request, 'rembolsoadmin.html')

def empleado(request):
    return render(request, 'empleadosadmin.html')

def inventario(request):
    return render(request, 'inventarioadmin.html')

def login(request):
    return render(request, 'login.html')
# Create your views here.
