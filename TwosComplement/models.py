from queue import Empty
from django.db import models
from django.template.defaultfilters import slugify


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


class UserProfile(models.Model):

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=45)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=254)
    gender = models.CharField(max_length=30, choices=Gender, default=None)
    sexualPreference = models.CharField(max_length=30, choices=Sexual_Preference, default=None)

    def __str__(self):
        return self.username


class Matches(models.Model):

    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user2")
    compatibilityScore = models.IntegerField()

    def __str__(self):
        return self.user1.username


class Questionnaire(models.Model):

    #user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    #answer1 = models.IntegerField()
    #answer2 = models.IntegerField()
    #answer3 = models.IntegerField()
    #answer4 = models.IntegerField()
    #answer5 = models.IntegerField()
    #answer6 = models.IntegerField()
    #answer7 = models.IntegerField()
    #answer8 = models.IntegerField()
    #answer9 = models.IntegerField()
    #answer10 = models.IntegerField()

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    Q1 = models.CharField(max_length=30, choices=Q1Choices, default=None)
    Q2 = models.CharField(max_length=30, choices=Q2Choices, default=None)
    Q3 = models.CharField(max_length=30, choices=Q3Choices, default=None)
    Q4 = models.CharField(max_length=30, choices=Q4Choices, default=None)
    Q5 = models.CharField(max_length=30, choices=Q5Choices, default=None)
    Q6 = models.CharField(max_length=30, choices=Q6Choices, default=None)
    Q7 = models.CharField(max_length=30, choices=Q7Choices, default=None)
    Q8 = models.CharField(max_length=30, choices=Q8Choices, default=None)
    Q9 = models.CharField(max_length=30, choices=Q9Choices, default=None)
    Q10 = models.CharField(max_length=30, choices=Q10Choices, default=None)
    def __str__(self):
        return self.user.username
