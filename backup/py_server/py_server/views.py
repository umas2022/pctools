import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
 
def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def home(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'home.html', context)

@csrf_exempt
def home_copy_to_one(request):
    context          = {}
    if request.POST:
        context['getInput'] = request.POST.get("inputPath")
        context['getOutput'] = request.POST.get("outputPath")
    print(request.POST)
    print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")