from django import forms
from django.forms import CharField

from TwosComplement.models import UserProfile, Questionnaire

Gender = ['Male', 'Female', 'Prefer not to specify']
Sexual_Preference = ['Male', 'Female']


class UserForm(forms.ModelForm):
    #username = forms.CharField(max_length=30, required=True, help_text="Username already in use")
    #password = forms.CharField(widget=forms.PasswordInput())
    #age = forms.IntegerField(required=True, help_text="Please enter your age number")
    #email = forms.EmailField(max_length=45, required=True, help_text="Please enter a valid email address")
    #name = forms.CharField(max_length=30, required=True, help_text="Please enter your name")
    #phone = forms.CharField(max_length=11, required=True, help_text="Please enter a valid number and format")
    #photo = forms.ImageField()
    #bio = forms.CharField(max_length=254, help_text="Please enter a short description about yourself")
    #gender = forms.CharField(label='Gender', widget=forms.Select(choices=Gender))
    #sexualPreference = forms.CharField(label='Sexual preference', widget=forms.Select(choices=Sexual_Preference))

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'age', 'email', 'name', 'phone',
                  'photo', 'bio', 'gender', 'sexualPreference',)

