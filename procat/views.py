from django.shortcuts import render,render_to_response
from django.core.context_processors import request
from django.http import HttpResponse
from procat.forms import CategoryForm,ProductsForm
from procat.models import Category,Products
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    return render_to_response('index.html')

def showCat(request,arg={}):
    cats = Category.objects.all()    
    catform = CategoryForm()
    context = {
               'request':showRequest(request),
               'catList':cats,  
               'catform':catform,
               }
    if arg:context.update(arg)    
    return render_to_response('catManage.html',context)

def addCat(request):
    if request.method =='POST':
        catform = CategoryForm(request.POST,request.FILES)
        has_saved = False  
        if catform.is_valid():                                  
            try:           
                c = Category( name= catform.cleaned_data['name'],
                              img = request.FILES['img'])
                c.save()
                has_saved =True                
            except KeyError:pass
    return showCat(request,{'result':has_saved})


def delCat(request):
    if request.method == 'POST':        
        #if catform.is_valid():           
        c = Category.objects.get(id =request.POST.get('catId')) 
        c.img.delete(save = True)       
        c.delete()                        
    return showCat(request)

def addPro(request):
    if request.method == 'POST':
        proform = ProductsForm(request.POST, request.FILES)        
        if proform.is_valid():print('data is valid') 
        else :print('data isn \' t valid')
        data = proform.cleaned_data
        print (data)
        p = Products(
                   name=request.POST.get('productName'),
                   price=request.POST.get('productPrice'),
                   description=request.POST.get('productDescription'),
                   img = request.FILES['img'],
                   )
        p.save()     
        print ('has saved !!')      
        catList = request.POST.getlist('category')
        if catList:
            for i in catList:
                p.category.add(Category.objects.get(name=i)) 
                          
    return showPro(request, {})


def delPro(request):
    if request.method == 'POST':
        print('recieve POST ')
        proform = ProductsForm(request.POST)
        print ('created form')
        print('form is valid')
        p = Products.objects.get(id=request.POST.get('proId'))
        p.img.delete(save=True)
        p.delete()  
    return showPro(request, {}) 

    

@csrf_exempt
def showPro(request,arg={}):    
    pros = Products.objects.all()
    cats = Category.objects.all()
    pform = ProductsForm({'name':'somename','price':122,'description':'some description'})
    if request.GET.get('orderby',False):        
            pros.order_by('')
            
            
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

    
