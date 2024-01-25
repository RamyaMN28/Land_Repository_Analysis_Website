from django.contrib.auth.forms import UserCreationForm
from .models import AadharVerification
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields =['username','email','password1','password2']

class AadharVerificationForm(forms.ModelForm):
    class Meta:
        model = AadharVerification
        fields = ['aadhar_number', 'name']
        widgets = {
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Aadhar Number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Full Name'}),
        }

    def clean_aadhar_number(self):
        # Add additional validation logic for Aadhar number if needed
        aadhar_number = self.cleaned_data['aadhar_number']
        # Your custom validation logic here, if required
        return aadhar_number
    
