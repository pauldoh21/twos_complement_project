from django.db import models


class User(models.Model):
    NAME_MAX_LENGTH = 128

    username = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    password = models.CharField(min_length=8, max_length=30)
    age = models.IntegerField(max_length=2)
    email = models.EmailField(max_length=45)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    phone = models.IntegerField(default=11)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=254)
    gender = models.CharField(max_length=30)
    sexualPreference = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Matches(models.Model):

    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)
    compatibilityScore = models.IntegerField(max_length=2)

    def __str__(self):
        return self.title


class Questionnaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answer1 = models.IntegerField(max_length=2)
    answer2 = models.IntegerField(max_length=2)
    answer3 = models.IntegerField(max_length=2)
    answer4 = models.IntegerField(max_length=2)
    answer5 = models.IntegerField(max_length=2)
    answer6 = models.IntegerField(max_length=2)
    answer7 = models.IntegerField(max_length=2)
    answer8 = models.IntegerField(max_length=2)

    def __str__(self):
        return self.user.username
