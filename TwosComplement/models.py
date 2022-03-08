from queue import Empty
from django.db import models
from django.template.defaultfilters import slugify


Gender = (('0',''),('1','Male'),('2', 'Female'),('3', 'Prefer not to specify'))
Sexual_Preference = (('0',''),('1','Male'),('2', 'Female'))

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
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    answer1 = models.IntegerField()
    answer2 = models.IntegerField()
    answer3 = models.IntegerField()
    answer4 = models.IntegerField()
    answer5 = models.IntegerField()
    answer6 = models.IntegerField()
    answer7 = models.IntegerField()
    answer8 = models.IntegerField()
    answer9 = models.IntegerField()
    answer10 = models.IntegerField()

    def __str__(self):
        return self.user.username
