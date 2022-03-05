from django import forms
from TwosComplement.models import User, Matches, Questionnaire

Gender=['Male','Female','Prefer not to specify']
Sexual_Preference=['Male','Female']

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128, unique=True,required=True, help_text="Username already in use")
    password = forms.PasswordInput(max_length=128, unique=True,required=True, help_text="Please enter password")
    age = forms.IntegerField(max_length=2, required= True, help_text="Please enter your age number")
    email = forms.EmailField(max_length=45, required=True, help_text="Please enter a valid email address")
    name = forms.CharField(max_length=128, required=True, help_text="Please enter your name")
    phone = forms.IntegerField(default=11, help_text="Please enter a valid number and format")
    photo = forms.ImageField(upload_to='profile_images', blank=True,)
    bio = forms.CharField(max_length=254, help_text="Please enter a short description about yourself")
    gender = forms.CharField(label='Gender', widget=forms.Select(choices=Gender))
    sexualPreference = forms.CharField(label='Sexual preference', widget=forms.Select(choices=Sexual_Preference))

    class Meta:
        model = User
        fields = ('username','password,','age','email','name','phone',
        'photo','bio','gender','sexualPreference')












