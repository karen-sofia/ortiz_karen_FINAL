from django.shortcuts import render,redirect
from .models import Inscritos,Instituciones
from .forms import FormInscritos,FormInstituciones
from .serializers import InscritosSerializer,InstitucionesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404,JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def agregarInstituciones(request):
    form = FormInstituciones()

    if (request.method == 'POST'):
        form = FormInstituciones(request.POST)
        if form.is_valid():
            form.save()
        return index(request)

    data = {'form' : form}
    return render(request, 'agregar.html', data)

def agregarInscritos(request):
    form = FormInscritos()

    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
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


@api_view(['GET','POST'])
def listarInstituciones(request):
    if request.method == 'GET':
        institucion = Instituciones.objects.all()
        serial = InstitucionesSerializer(institucion,many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionesSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT','DELETE'])
def InstitucionesDetalle(request,id):
    try:
        institucion = Instituciones.objects.get(pk=id)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #PARA OBTENER LOS DATOS
    if request.method == 'GET':
        serial = InstitucionesSerializer(institucion)
        return Response(serial.data)
    
    #PARA EDITAR DATOS
    if request.method == 'PUT':
        serial = InstitucionesSerializer(institucion,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #PARA BORRAR LOS DATOS
    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListarInscritos_class(APIView):
    def get(self, request):
        inscritos = Inscritos.objects.all()
        serial = InscritosSerializer(inscritos, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class InscritosDetalle_class(APIView
                             ):
    def get_object(self, id):
        try:
            return Inscritos.objects.get(pk=id)
        except Inscritos.DoesNotExist:
            raise Http404()

    def get(self, request, id):
        inscrito = self.get_object(id)
        serial = InscritosSerializer(inscrito)
        return Response(serial.data)

    def put(self, request, id):
        inscrito = self.get_object(id)
        serial = InscritosSerializer(inscrito,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









