from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Producto

class Home(View):
	def get(self,request):
		return render(request,'main/home.html')

class Perfil(View):
	def get(self,request):
		return render(request,'main/perfil.html')

	def post(self,request):
		new_p=Producto()
		new_p.nombre= request.POST.get('nombre')
		new_p.desc= request.POST.get('desc')
		new_p.precio=request.POST.get('precio')
		new_p.usuario=request.user
		new_p.save()
		return redirect('Perfil')

