from django import forms
from django.forms import CharField

from TwosComplement.models import UserProfile, Questionnaire

Gender = (('0',''),('1','Male'),('2', 'Female'),('3', 'Prefer not to specify'))
Sexual_Preference = (('0',''),('1','Male'),('2', 'Female'))

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, help_text="Username" )
    password = forms.CharField(widget=forms.PasswordInput(),help_text="Password")
    age = forms.IntegerField(required=True, help_text="Age")
    email = forms.EmailField(max_length=45, required=True, help_text="Email")
    name = forms.CharField(max_length=30, required=True, help_text="Name")
    phone = forms.CharField(max_length=11, required=True, help_text="Phone number")
    photo = forms.ImageField(help_text="Profile image",required=False)
    bio = forms.CharField(max_length=254, help_text="Bio")
    gender = forms.CharField(label='Gender', widget=forms.Select(choices=Gender),help_text="Gender")
    sexualPreference = forms.CharField(label='Sexual preference', widget=forms.Select(choices=Sexual_Preference),help_text="Sexual preference")

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'age', 'email', 'name', 'phone',
                  'photo', 'bio', 'gender', 'sexualPreference',)

