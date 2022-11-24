from django.shortcuts import render, redirect

# Create your views here.
from inapp.forms import UpdateForm
from inapp.models import Product

def home(request):
    return render(request,'home.html')

def index(request):
    product=Product.objects.all()
    return render(request,'index.html',{'prod_ct':product})

def Detail(request,id):
    pro=Product.objects.get(id=id)
    return render(request,'detail.html',{'data':pro})

def add_product(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        image=request.FILES['img']
        product=Product(name=name,desc=desc,year=year,img=image)
        product.save()
        return redirect('/')
    return render(request,'add_pro.html')


#update
def update(request,id):
    product=Product.objects.get(id=id)
    form=UpdateForm(request.POST or None,request.FILES,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'product':product})

def delete(request,id):
    if request.method=='POST':
        product=Product.objects.get(id=id)
        product.delete()
        return redirect('/')
    return render(request,'delete.html')
