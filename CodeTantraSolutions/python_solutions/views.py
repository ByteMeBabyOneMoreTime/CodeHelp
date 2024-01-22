from django.shortcuts import render, HttpResponse
from .models import Python_data
from django.template import loader
# Create your views here.
def Answers(request):
    data = Python_data.objects.all().values()
    print(data)
    template = loader.get_template('python.html')
    context = {
        'context': data,
    }
    return HttpResponse(template.render(context,request))