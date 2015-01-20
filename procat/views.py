from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.http import HttpResponse
from procat.forms import CategoryForm,ProductsForm
from procat.models import Category,Products
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    return render_to_response('index.html')
@csrf_exempt
def showCat(request,**arg):
    cats = Category.objects.all()    
    context = {'request':showRequest(request),'catList':cats}
    context.update( arg)    
    return render_to_response('catManage.html',context)

@csrf_exempt
def addCat(request):
    if request.method =='POST':
        catform = CategoryForm(request.POST)
        has_saved = False        
        if catform.is_valid():                       
            try:           
                Category(name=request.POST.get('name')).save()
                has_saved =True                
            except KeyError:pass
    return showCat(request,{'result':has_saved})

@csrf_exempt
def delCat(request):
    if request.method == 'POST':
        catform = CategoryForm(request.POST)
        if catform.is_valid():           
            c = Category.objects.get(id =request.POST.get('catId'))
            c.delete()                
    return showCat(request)

def showPro(request,**arg):    
    
    pros = Products.objects.all()
    if request.GET。get('orderby'):
        pros.order_by(request.GET。get('orderby'))
    context = {'products':pros}
    return render_to_response('proManage.html',context)
         
          
            
        

def showRequest(request):
    values = request.META.items() 
    html = []
    for k, v in values:
        html.append('%s => %s ' % (k, v))
    return html

    
