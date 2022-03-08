from django import forms
from django.forms import CharField

from TwosComplement.models import UserProfile, Questionnaire

Gender = (('0',''),('1','Male'),('2', 'Female'),('3', 'Prefer not to specify'))
Sexual_Preference = (('0',''),('1','Male'),('2', 'Female'))

Q1Choices = (('0',"Python"), ('1',"java"), ('2',"C and related"), ('3',"other"))
Q2Choices = (('0',"VSCode"),('1',"Eclipse"),('2',"IntelliJ"),('3',"PyCharm"))
Q3Choices = (('0',"< 1 year"),('1',"1-3 years"), ('2',"3-5 years"), ('3',"5+ years"))
Q4Choices = (('0',"Apps"),('1',"Databases"),('2',"Games"),('3',"Security"))#look over options
Q5Choices = (('0',"Artifical Intelligence"),('2',"Graphics"),('3',"Database Management Systems"),('4',"Human-Computer Interaction(HCI)"))
Q6Choices = (('0',"Capricorn"),('1',"Aquarius"),('2',"Pisces"),('3',"Aries"),('4',"Taurus"),('5',"Gemimi"),('6',"Cancer"),('7',"Leo"),('8',"Virgo"),('9',"Libra"),('10',"Scorpio"),('11',"Sagittarius"))
Q7Choices = (('0',"Extrovert"),('1',"Ambivert"),('2',"Introvert"))
Q8Choices = (('0', "Physical Touch"),('1',"Word of Affirmation"),('2',"Quality Time"),('3',"Gift Giving"),('4',"Acts of Service"))
Q9Choices = (('0',"Sports"),('1',"Travel"),('2',"Working"),('3',"Sleeping"),('4',"Clubbing"),('5',"TV/Movies"),('6',"Cooking"),('7',"Chilling"))
Q10Choices = (('0',"Italian"),('1',"Indian"),('2',"Chinese"),('3',"Mexican"),('4',"other"),('5',"No Preference"))

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

class QuestionnaireForm(forms.ModelForm):
    Q1 = forms.CharField(label="What is your favourite programming language?", widget=forms.Select(choices=Q1Choices),help_text="What is your favourite language?")
    Q2 = forms.CharField(label="What IDE do you use the most?", widget=forms.Select(choices=Q2Choices),help_text="What IDE do you use the most?")
    Q3 = forms.CharField(label="How long have you been coding for?", widget=forms.Select(choices=Q3Choices),help_text="How long have you been coding for?")
    Q4 = forms.CharField(label="What do enjoy developing the most?", widget=forms.Select(choices=Q4Choices),help_text="What do enjoy developing the most?")
    Q5 = forms.CharField(label="What area of Computer Science intrigues you the most?", widget=forms.Select(choices=Q5Choices),help_text="What area Computer Science intrigues you the most?")
    Q6 = forms.CharField(label="What is your star sign?", widget=forms.Select(choices=Q6Choices),help_text="Whats your star sign?")
    Q7 = forms.CharField(label="How would you describe yourself?", widget=forms.Select(choices=Q7Choices),help_text="How would you describe yourself?")
    Q8 = forms.CharField(label="What is your love language?", widget=forms.Select(choices=Q8Choices),help_text="What is your love language?")
    Q9 = forms.CharField(label="What does a typical weekend look like for you?", widget=forms.Select(choices=Q9Choices),help_text="What does a typical weekend look like for you?")
    Q10 = forms.CharField(label="What is your favourite cuisine?",widget=forms.Select(choices=Q10Choices),help_text="What is your favourite cuisine?")
   
    class Meta:
            model = Questionnaire
            fields = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10',)
