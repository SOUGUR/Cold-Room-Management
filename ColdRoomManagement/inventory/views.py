from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from inventory.models import Material
from inventory.forms import MaterialForm
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_material(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.added_by = request.user
            material.save()
            return redirect('list_materials')
    else:
        form = MaterialForm()
    return render(request, 'inventory/add_material.html', {'form': form})

@login_required
def list_materials(request):
    materials = Material.objects.all()
    today = timezone.now().date()
    return render(request, 'inventory/list_materials.html', {'materials': materials, 'today': today})

@login_required
def upcoming_expiries(request):
    today = timezone.now().date()
    next_month = today + timezone.timedelta(days=30)
    expiring_soon = Material.objects.filter(expiry_date__range=(today, next_month))
    return render(request, 'inventory/upcoming_expiries.html', {'expiring_soon': expiring_soon})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('add_material')
    else:
        form = UserRegisterForm()
    return render(request, 'inventory/register.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'inventory/login.html'
    authentication_form = UserLoginForm

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def delete_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    material.delete()
    messages.success(request, f'Material {material.name} deleted successfully.')
    return redirect('inventory/list_materials')
