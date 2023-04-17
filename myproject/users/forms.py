from django import forms
from django.contrib.auth.forms import Forms
from django.contrib.auth.models import User

class HomeForm(Forms):
    fullname=forms.CharField(max_length=101)
    city=forms.CharField(max_length=101)
    area=forms.CharField(max_length=101)
    pincode=forms.CharField(max_length=101)
    emailid=forms.CharField(max_length=101)
    password1=forms.CharField(max_length=101)
    password2=forms.CharField(max_length=101)

    class Meta:
        model=User
        fields=["fullname","city","area","pincode","email","password1","password2"]
        