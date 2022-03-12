from django import forms
from django.contrib.auth.models import User
from django.forms import CharField

from TwosComplement.models import UserProfile, Questionnaire

Gender = (('0','Choose an option'),('1','Male'),('2', 'Female'),('3', 'Prefer not to specify'))
Sexual_Preference = (('0','Choose an option'),('1','Male'),('2', 'Female'),('3', 'No preference'))

Q1Choices = (('0',''),('1',"Python"), ('2',"java"), ('3',"C and related"), ('4',"other"))
Q2Choices = (('0',''),('1',"VSCode"),('2',"Eclipse"),('3',"IntelliJ"),('4',"PyCharm"))
Q3Choices = (('0',''),('1',"< 1 year"),('2',"1-3 years"), ('3',"3-5 years"), ('4',"5+ years"))
Q4Choices = (('0',''),('1',"Apps"),('2',"Databases"),('3',"Games"),('4',"Security"))#look over options
Q5Choices = (('0',''),('1',"Artifical Intelligence"),('2',"Graphics"),('3',"Database Management Systems"),('4',"Human-Computer Interaction(HCI)"))
Q6Choices = (('0',''),('1',"Capricorn"),('2',"Aquarius"),('3',"Pisces"),('4',"Aries"),('5',"Taurus"),('6',"Gemimi"),('7',"Cancer"),('8',"Leo"),('9',"Virgo"),('10',"Libra"),('11',"Scorpio"),('12',"Sagittarius"))
Q7Choices = (('0',''),('1',"Extrovert"),('2',"Ambivert"),('3',"Introvert"))
Q8Choices = (('0',''),('1', "Physical Touch"),('2',"Word of Affirmation"),('3',"Quality Time"),('4',"Gift Giving"),('5',"Acts of Service"))
Q9Choices = (('0',''),('1',"Sports"),('2',"Travel"),('3',"Working"),('4',"Sleeping"),('5',"Clubbing"),('6',"TV/Movies"),('7',"Cooking"),('8',"Chilling"))
Q10Choices = (('0',''),('1',"Italian"),('2',"Indian"),('3',"Chinese"),('4',"Mexican"),('5',"other"),('6',"No Preference"))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=True)
    name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=11, required=True)
    photo = forms.ImageField(required=False)
    bio = forms.CharField(max_length=254)
    gender = forms.CharField(label='Gender', widget=forms.Select(choices=Gender))
    sexualPreference = forms.CharField(label='Sexual preference', widget=forms.Select(choices=Sexual_Preference))

    class Meta:
        model = UserProfile
        fields = ('age', 'name', 'phone', 'photo', 'bio', 'gender', 'sexualPreference',)


class QuestionnaireForm(forms.ModelForm):

    Q1 = forms.CharField(label="What is your favourite programming language?", widget=forms.Select(choices=Q1Choices),help_text="What is your favourite programming language?")
    Q2 = forms.CharField(label="What IDE do you use the most?", widget=forms.Select(choices=Q2Choices),help_text="What IDE do you use the most?")
    Q3 = forms.CharField(label="How long have you been coding for?", widget=forms.Select(choices=Q3Choices),help_text="How long have you been coding for?")
    Q4 = forms.CharField(label="What do you enjoy developing the most?", widget=forms.Select(choices=Q4Choices),help_text="What do enjoy developing the most?")
    Q5 = forms.CharField(label="What area of Computer Science intrigues you the most?", widget=forms.Select(choices=Q5Choices),help_text="What area Computer Science intrigues you the most?")
    Q6 = forms.CharField(label="What is your star sign?", widget=forms.Select(choices=Q6Choices),help_text="Whats your star sign?")
    Q7 = forms.CharField(label="How would you describe yourself?", widget=forms.Select(choices=Q7Choices),help_text="How would you describe yourself?")
    Q8 = forms.CharField(label="What is your love language?", widget=forms.Select(choices=Q8Choices),help_text="What is your love language?")
    Q9 = forms.CharField(label="What does a typical weekend look like for you?", widget=forms.Select(choices=Q9Choices),help_text="What does a typical weekend look like for you?")
    Q10 = forms.CharField(label="What is your favourite cuisine?",widget=forms.Select(choices=Q10Choices),help_text="What is your favourite cuisine?")
   
    class Meta:
        model = Questionnaire
        fields = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10',)
