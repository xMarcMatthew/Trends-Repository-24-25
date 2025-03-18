from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def members(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
