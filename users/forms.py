from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email',
            'password1', 'password2',
            'phone_number', 'dob', 'gender', 'emotion', 'terms_agree'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
