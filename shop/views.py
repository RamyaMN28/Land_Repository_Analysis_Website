from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from shop.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import DiscountCode
from .form import AadharVerificationForm
import json
# Create your views here.

def home(request):
    properties = Property.objects.filter(trending=1)
    return render(request,"shop/index.html",{"properties":properties})

def payment_page(request):
    return render(request, 'shop/payment_page.html') 

# views.py
from django.shortcuts import render, redirect
from .form import AadharVerificationForm
from .models import AadharVerification

def aadhar_verification(request):
    if request.method == 'POST':
        form = AadharVerificationForm(request.POST)
        if form.is_valid():
            # Dummy Aadhar verification logic (replace this with a real implementation)
            aadhar_number = form.cleaned_data['aadhar_number']

            # Dummy validation: Check if Aadhar number is a 12-digit number
            if len(aadhar_number) == 12 and aadhar_number.isdigit():
                aadhar_verified=1
                # Successful verification
                # Save the Aadhar details to the database
                AadharVerification.objects.create(
                    aadhar_number=aadhar_number,
                    name=form.cleaned_data['name']
                
                )

                return redirect('payment_in_progress')  # Redirect to the payment page
            else:
                # Failed verification
                aadhar_verified=1
                form.add_error('aadhar_number', 'Invalid Aadhar number')
    else:
        form = AadharVerificationForm()

    return render(request, 'shop/aadhar_verification.html', {'form': form})

# Import your Message modelS
#def display_message_content(request, msg_id):
    # Retrieve the Message object with the specified msg_id
 #   message = get_object_or_404(Message, msg_id=msg_id)

    # Pass the entire message instance to the template in the context
  #  context = {'message': message}

    # Render the template with the context
   # return render(request, 'messagee.html', context)



def payment_in_progress(request):
    return render(request, 'shop/payment_in_progress.html')

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
                     # Apply discount logic to the cart
                    if request.session.get('discount_applied'):
                        discount_percentage = request.session.get('discount_percentage', 0)
                        
                        # Update cart items with the applied discount
                        for cart_item in Cart.objects.filter(user=request.user, property_id=property_id):
                            cart_item.price -= cart_item.price * (discount_percentage)
                            cart_item.save()

                                                # Clear discount information from the session
                        del request.session['discount_applied']
                        del request.session['discount_percentage']
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
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        discount_code = request.POST.get('discount_code')
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in first
            login(request, user)
            messages.success(request, "Logged in Successfully")

            # Check and apply discount code if provided
            if discount_code:
                try:
                    code_obj = DiscountCode.objects.get(code=discount_code)
                    # Apply discount logic here
                    # ...

                    # For demonstration purposes, let's just set a session variable
                    request.session['discount_applied'] = True
                    request.session['discount_percentage'] = code_obj.percentage_discount
                    messages.success(request, "Congratulations! You have applied a discount code.")
                except DiscountCode.DoesNotExist:
                    # Handle invalid discount code
                    messages.error(request, "Invalid Discount Code")
            else:
                messages.success(request, "you have not applied any discount code")

            return redirect("/")
        else:
            messages.error(request, "Invalid User Name or Password")

    return render(request, "shop/login.html")

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

def view_payment_details(request):
    # Add logic to fetch and display payment details
    # You can pass additional context to the template if needed
    return render(request, 'payment_details.html')



