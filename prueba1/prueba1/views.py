from django.shortcuts import render

def index (request):
    template_name= 'index.html'
    nombres=['Jose','Leonardo','Carlos','Flor']
    context= {'nombre': 'Ceci'}
    return render(request,template_name,context=context )