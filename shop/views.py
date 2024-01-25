from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from shop.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
# Create your views here.
#i edited this file
def home(request):
    properties = Property.objects.filter(trending=1)
    return render(request,"shop/index.html",{"properties":properties})

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"fav":fav})
    else:
        messages.warning(request,"Login to View Cart")
        return redirect("/")

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        messages.warning(request,"Login to View Cart")
        return redirect("/")
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        messages.warning(request,"Login to View Cart")
        return redirect("/")

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def remove_fav(request,fid):
    item=Favourite.objects.get(id=fid)
    item.delete()
    return redirect("/favviewpage")

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            property_id=data['pid']
            property_status=Property.objects.get(id=property_id)
            if property_status:
                if Favourite.objects.filter(user=request.user.id,property_id=property_id):
                    return JsonResponse({'status':'Property Already in Favourite'},status=200)
                else:
                    Favourite.objects.create(user=request.user,property_id=property_id)
                    return JsonResponse({'status':'Property Added to Favourite'},status=200)
           # print(request.user.id)
        else:  
            return JsonResponse({'status':'Login to Add Favourite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            property_qty=1
            property_id=data['pid']
           # print(request.user.id)
            property_status=Property.objects.get(id=property_id)
            if property_status:
                if Cart.objects.filter(user=request.user.id,property_id=property_id):
                    return JsonResponse({'status':'Property Already in cart'},status=200)
                else:
                    Cart.objects.create(user=request.user,property_id=property_id,property_qty=property_qty)
                    return JsonResponse({'status':'Property Added to Cart success'},status=200)

           # return JsonResponse({'status':'Added to Cart'},status=200)

        else:
            
            return JsonResponse({'status':'Login to Add Cart'},status=200)
        
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)
def logout_page(request):
    if request.user.is_authenticated:
        messages.success(request,"Logged out successfully")
        logout(request)
        return redirect("/")
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
     if request.method=="POST":
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            messages.success(request,"Logged in Successfully")
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect("/login")
    return render(request,"shop/login.html")
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now...!")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def PlotType(request):
    property_type=PropertyType.objects.filter(status=0)
    return render(request,"shop/PlotType.html",{"property_type":property_type})
def PlotTypeviews(request,name):
    if(PropertyType.objects.filter(name=name,status=0)):
        properties = Property.objects.filter(property_type__name=name)
        return render(request,"shop/properties/index.html",{"properties":properties,"property_name":name})
    else:
        #messages.warning(request,"No such PropertyType")
        return redirect('PlotType')
def plot_details(request,cname,pname):
    if(PropertyType.objects.filter(name=cname,status=0)):
        if(Property.objects.filter(name=pname,status=0)):  
            properties=Property.objects.filter(name=pname,status=0).first()
            return render(request,"shop/properties/plot_details.html",{"properties":properties})
        else: 
            messages.warning(request,"No such Property")
            return redirect('PlotType')
    else:
        messages.warning(request,"No such PropertyType")
        return redirect('PlotType')

