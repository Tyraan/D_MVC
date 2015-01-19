from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.http import HttpResponse

def index(request):    
    return render_to_response('index.html')
def showCat(request):        
    return render_to_response('catManage.html',{'request':showRequest(request)})


def addCat(request):
    return 

def showRequest(request):
    values = request.META.items()    
    html = []
    for k, v in values:
        html.append('%s => %s ' % (k, v))
    return html

    
