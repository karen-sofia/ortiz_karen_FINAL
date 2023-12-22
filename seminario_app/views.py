from django.shortcuts import render
from .models import Instituciones, Inscritos
from .forms import FormInstituciones, FormInscritos
from django.http import JsonResponse
from .serializers import InstitucionesSerializer, InscritosSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def agregarInstituciones(request):
    form = FormInstituciones()

    if (request.method == 'POST'):
        form = FormInstituciones(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)

    data = {'form' : form}
    return render(request, 'agregar.html', data)

def agregarInscritos(request):
    form = FormInscritos()

    if (request.method == 'POST'):
        form = FormInscritos(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)

    data = {'form' : form}
    return render(request, 'agregar.html', data)

def perfil(request):
    per = {
        'id' : 1,
        'nombre' : 'Karen Ortiz',
        'email' : 'karen.ortiz08@inacapmail.cl',
        'sueldo' : '0'
    }
    return JsonResponse(per)


def listarInstituciones(request):


def listarInscritos(request):
