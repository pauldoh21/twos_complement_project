import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twos_complement_project.settings')

import django

django.setup()
from TwosComplement.models import UserProfile, Matches, Questionnaire

random.seed(1564)


def populate():
    users = [
        {"username": "", "password": "", "age": 0, "email": "", "name": "", "phone": "", "photo": "", "bio": "",
         "gender": "", "sexualPreference": ""},
        {"username": "RGreen19", "password": "", "age": 19, "email": "rgreen19@gmail.com", "name": "Rachel Green",
         "phone": "075555555", "photo": "", "bio": "Hello", "gender": "F", "sexualPreference": ""},
        {"username": "TLuke21", "password": "", "age": 21, "email": "tluke21@gmail.com", "name": "Tom Luke",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "M", "sexualPreference": ""},
        {"username": "CTribbiani32", "password": "", "age": 32, "email": "ctribbiani22@gmail.com",
         "name": "Chandler Tribbiani",
         "phone": "075555557", "photo": "", "bio": "Hello", "gender": "M", "sexualPreference": ""},
    ]

    questionnaires = []

    for i in range(len(users)):
        questionnaires.append({"user": users[i], "answers": {"ans1": random.randint(0, 3), "ans2": random.randint(0, 3),
                                                             "ans3": random.randint(0, 3), "ans4": random.randint(0, 3),
                                                             "ans5": random.randint(0, 3),
                                                             "ans6": random.randint(0, 3), "ans7": random.randint(0, 3),
                                                             "ans8": random.randint(0, 3),
                                                             }})

    for user in users:
        u = add_user(user["username"], user["password"], user["age"], user["email"], user["name"], user["phone"],
                     user["photo"], user["bio"], user["gender"], user["sexualPreference"])
        for q in questionnaires:
            add_questionnaire(u, q["answers"])


def add_user(username, password, age, email, name, phone, photo, bio, gender, sexualPreference):
    u = UserProfile.objects.get_or_create()[0]

    return u


def add_questionnaire(user, answers):
    q = Questionnaire.objects.get_or_create()[0]

    return q


populate()
