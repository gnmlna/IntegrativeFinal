from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Applicant



class ApplicantForm(forms.ModelForm):
    
    class Meta:
        model = Applicant
        fields = ['name', 'address','job', 'income', 'childNumber','civilStatus', 'gender', 'appdate', 'apptime','status']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'}),
            'income': forms.TextInput(attrs={'class': 'form-control'}),
            'childNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'civilStatus': forms.Select(attrs={'class': 'form-check'},
                                        choices=Applicant.CIVIL_STATUS),
            'gender': forms.Select(attrs={'class': 'form-check'},
                                    choices=Applicant.GENDER_CHOICES),
            'appdate': forms.TextInput(attrs={'class': 'form-control'}),
            'apptime': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select appointment time'},
                                    choices=Applicant.TIME_CHOICES),
            'status': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

