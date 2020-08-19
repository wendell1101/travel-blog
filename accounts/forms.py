from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile
from django import forms

# Create your models here.
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Profile
        fields = ['bio','slug','image','cover_image']
       