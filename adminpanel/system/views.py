from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import Clients
from django.contrib.auth.decorators import login_required


# Create your views here.

@never_cache
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username , password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            elif user.is_superuser :
                return redirect('adminpage')
            else:            
                messages.error(request, "invalid credentials")  
        return render(request, 'login.html')
    return redirect('home')
        
@never_cache    
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminpage')
        
        messages.success(request, "you are logged in")
        return render(request, 'home.html',)
    return redirect('user_login')


@never_cache
def user_logout(request):
    logout (request)    
    return redirect ("user_login")

def user_signup(request):
    if request.POST:
        usernames=request.POST.get('inputuser')
        passwords=request.POST.get('inputpassword')
        user=Clients.objects.create_user(username=usernames,password=passwords)
        messages.success(request, "you have successfully registered")
    
    return render(request,'signup.html',)

def adminpage(request):
    if request.user.is_superuser :
        print('admin')
        users=Clients.objects.all().exclude(is_superuser=True)
        return render(request, 'admin.html', {'users': users})
    
    print('else')
    return redirect('user_login')
def createuser(request):
   if request.user.is_superuser :
      if request.POST:
         usernames=request.POST.get('inputuser')
         passwords=request.POST.get('inputpassword')
         Age=request.POST.get('Age')
         user=Clients.objects.create_user(username=usernames,password=passwords,Age=Age)
         messages.success(request, "you have successfully registered")
         return redirect('adminpage')
         
      return render(request,'createuser.html')
    
   return redirect('user_login')

def delete(request,pk):
    user=Clients.objects.get(id=pk)
    user.delete()
    return redirect('adminpage')

def edit(request,pk):
    user=Clients.objects.get(id=pk)
    if request.POST:
        username=request.POST.get('inputuser')
        Age=request.POST.get('Age')
        user.username=username
        user.Age=Age
        user.save()
        return redirect('adminpage')
    
    return render(request,'edituser.html',{'user':user})
    
