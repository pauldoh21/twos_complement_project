
from django.db import models
from django.contrib.auth.models import User


Gender = (('0',''),('1','Male'),('2', 'Female'),('3', 'Prefer not to specify'))
Sexual_Preference = (('0',''),('1','Male'),('2', 'Female'),('3','No preference'))

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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=254)
    gender = models.CharField(max_length=30, choices=Gender, default=None)
    sexualPreference = models.CharField(max_length=30, choices=Sexual_Preference, default=None)

    def __str__(self):
        return self.user.username


class Matches(models.Model):

    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user2")
    compatibilityScore = models.IntegerField()

    def __str__(self):
        return self.user1.name

    class Meta:
        verbose_name_plural = 'Matches'


class Questionnaire(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
