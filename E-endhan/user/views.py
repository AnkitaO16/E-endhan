import re
from django.shortcuts import render,redirect
from .models import Destination
from .models import Contact
from django.contrib import messages

# Create your views here.
val = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")
def result(request):
    # print(request.session['value'])
    if request.user.is_superuser == True:
        s=Destination.objects.all()
        return render(request,"result.html",{"s":s})
    else:
        return render(request,"home.html")
def custmer(request):
    # print(request.session['value'])
    if request.user.is_superuser == True:
        s=Contact.objects.values('firstname','lastname','country','subject')
        return render(request,"custmer.html",{"s":s})
    else:
        return render(request,"home.html")


def add(request):
    
    if request.method=='POST':

        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        ammount = request.POST["ammount"]
        address = request.POST["address"]
        fuel = request.POST["fuel"]
        
        if name[0].isupper():
            if re.search(val,email):
                data_store = Destination(name=name,email=email,mobile=mobile,ammount=ammount,address=address,fuel=fuel)
                data_store.save()
                return redirect('final')
                
            else:
                messages.info(request,'Incorrect email')
                return redirect('home')
        else:
            messages.info(request,'Name must start with capital latter')
            return redirect('home') 

# for Contact_Us page
def Add1(request):
    
    if request.method=='POST':

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        country = request.POST["country"]
        subject = request.POST["subject"]
        
        
        if firstname[0].isupper():
            if lastname[0].isupper():
                data = Contact (firstname = firstname,lastname=lastname,country=country,subject=subject)
                data.save()
                return redirect('final')
                
            else:
                messages.info(request,'Lastname must start with Capital latter')
                return redirect('contact')
        else:
            messages.info(request,'FirstName must start with capital latter')
            return redirect('contact') 



        
        
def final(request):
    return render(request,"final.html")   


