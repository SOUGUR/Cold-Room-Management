from django.urls import path
from . import views
from .views import UserLoginView, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('add/', views.add_material, name='add_material'),
    path('', views.list_materials, name='list_materials'),
    path('expiries/', views.upcoming_expiries, name='upcoming_expiries'),
    path('delete/<int:material_id>/', views.delete_material, name='delete_material'),
]
