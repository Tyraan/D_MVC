from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.http import HttpResponse
from procat.forms import CategoryForm,ProductsForm
from procat.models import Category,Products
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    return render_to_response('index.html')
@csrf_exempt
def showCat(request,arg={}):
    cats = Category.objects.all()    
    context = {
               'request':showRequest(request),
               'catList':cats,  
               }    
    if arg:context.update(arg)    
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

@csrf_exempt
def addPro(request):
    if request.method =='POST':
        proform = ProductsForm(request.POST)
        has_saved = False
        if proform.is_valid():
            data = proform.cleaned_data
            p = Products(
                   name = request.POST.get('productName'),
                   price = request.POST.get('productPrice'),
                   description = request.POST.get('productDescription'), 
                   )
            p.save()           
            catList = request.POST.getlist('category')
            if catList:
                for i in catList:
                     p.category.add(Category.objects.get(name = i))
                  
    return showPro(request,{})


@csrf_exempt
def delPro(request):
    if request.method =='POST':
        proform = ProductsForm(request)
        if proform.is_valid():
            c = Products.objects.get(id =request.POST.get('proId'))
            c.delete()  
    return showPro(request,{})     

@csrf_exempt
def showPro(request,arg={}):    
    pros = Products.objects.all()
    cats = Category.objects.all()
    pform = ProductsForm({'name':'somename','price':122,'description':'some description'})
    if request.GET.get('orderby',False):        
        pros.order_by(request.POST['orderby'])
        if request.GET.get('order',True):
            pros.sort()
            
    context = {'proList':pros,
               'request':showRequest(request),
               'catList':cats,
               'pform':pform,               
               }    
    if arg:context.update(arg)
    return render_to_response('proManage.html',context)
          

            
        

def showRequest(request):
    html = []
    for k,v in request.POST.items():   
        html.append('%s ------->%s ' % (k,v))
    for k,v in request.GET.items() :
        html.append('%s >>>> %s' % (k,v))        
    for k,v in request.META.items():
        html.append('%s =====>%s ' % (k,v))
     

    return html

    
