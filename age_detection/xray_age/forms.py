from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from xray_age.models import Profile,Upload
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name','gender','weight','image','age')