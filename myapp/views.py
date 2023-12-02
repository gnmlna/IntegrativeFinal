from django.shortcuts import render, redirect  
from myapp.forms import ApplicantForm  
from myapp.models import Applicant 

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# this import is for flash messages
from django.contrib import messages
 
# Create your views here.  
from .forms import CreateUserForm

def register(request):  
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'You have been registered ' + user)
                return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context) 

def loginPage(request): 
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Invalid username or password.')

    context = {}
    return render(request,'login.html')

@login_required(login_url='login')    
def logoutUser(request): 
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add(request):  
    if request.method == "POST":  
        form = ApplicantForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = ApplicantForm()  
    return render(request,'index.html',{'form':form})  

@login_required(login_url='login')
def index(request):  
    applicants = Applicant.objects.all()  
    return render(request,"show.html",{'applicants':applicants}) 

@login_required(login_url='login')
def edit(request, id):  
    applicant = Applicant.objects.get(id=id)  
    return render(request,'edit.html', {'applicant':applicant})

@login_required(login_url='login')
def update(request, id):  
    applicant = Applicant.objects.get(id=id)  
    form = ApplicantForm(request.POST, instance = applicant)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'applicant': applicant})  
     
def destroy(request, id):  
    applicant = Applicant.objects.get(id=id)  
    applicant.delete()  
    return redirect("/")  


def show(request):  
    applicants = Applicant.objects.all()  
    return render(request,"show.html",{'applicants':applicants})

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')



