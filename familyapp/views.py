from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Familymodel

# Create your views here.

def listado_familia(request):
    template = loader.get_template('listado_familia.html')
    familiares = Familymodel.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return HttpResponse(template.render(context, request))