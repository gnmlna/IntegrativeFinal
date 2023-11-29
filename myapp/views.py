from django.shortcuts import render, redirect  
from myapp.forms import ApplicantForm  
from myapp.models import Applicant 
from django.contrib.auth.forms import UserCreationForm 
 
# Create your views here.  
from .forms import CreateUserForm

def register(request):  
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'register.html',context) 

def login(request):  
    return render(request,'login.html',context)
     
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
 
def index(request):  
    applicants = Applicant.objects.all()  
    return render(request,"show.html",{'applicants':applicants}) 

def edit(request, id):  
    applicant = Applicant.objects.get(id=id)  
    return render(request,'edit.html', {'applicant':applicant})  
 
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

def home(request):
    return render(request, 'home.html')



