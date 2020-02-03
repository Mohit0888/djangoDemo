from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth , User
# Create your views here.
def register(request):
   
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['user_name']
        email =request.POST['email']
        password =request.POST['password']
        confPassword =request.POST['confirm_password']
        if password == confPassword:
            if User.objects.filter(username=userName).exists():
                messages.info(request,'User Name Taken')
                return render(request,'register.html')    
            elif User.objects.filter(email=email).exists():   
                messages.info(request,'email already exist')
                return render(request,'register.html')
            else:   
                user = User.objects.create_user(username=userName,password=password,first_name=firstName,last_name=lastName,email=email)
                user.save(); 
                messages.info(request,'User Created') 
                return redirect('login') 
        else: 
            messages.info(request,'password not matching')  
            return render(request,'register.html')
             
    else:
        return render(request,'register.html')
        
def login(request):
    
    if request.method == 'POST':
        userName = request.POST['user_name']
        password =request.POST['password']

        user= auth.authenticate(username=userName,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['is_logged'] = True
            return redirect("home")
        else:    
            messages.info(request,"invalid Credentials")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    request.session.flush()
    auth.logout(request)
    return redirect('/')   

def home(request):
    if request.session.has_key('is_logged'):
        return redirect('/')   
        
     