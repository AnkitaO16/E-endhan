import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

val = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)"
# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        request.session['value'] = user.username
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
             
    
def register(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        

        if first_name[0].isupper():
            if last_name[0].isupper():
                if re.search(val,email):
                    if len(password2)>=6:
                        if password1==password2:
                            if User.objects.filter(username=username).exists():
                                messages.info(request,'Username Taken')
                                return redirect('register')

                            elif User.objects.filter(email=email).exists():
                                messages.info(request,'Email Taken')
                                return redirect('register')
                            user = User.objects.create_user( username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                            user=user.save();
                            print('User created')
                            return redirect('login')
                        else:
                            messages.info(request,'password is not matching')
                            return redirect('register')
                    else:
                        messages.info(request,'password is too small')
                        return redirect('register')
                else:
                    messages.info(request,'Incorrect email')
                    return redirect('register')        
            else:
                messages.info(request,'Last name must start with capital latter')
                return redirect('register')
        else:
            messages.info(request,'First name must start with capital latter')
            return redirect('register')
        # turn redirect('home')    
    else:
         return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
    
   
