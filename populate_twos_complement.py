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
         "gender": "0", "sexualPreference": "0"},
        {"username": "RGreen19", "password": "deez", "age": 19, "email": "rgreen19@gmail.com", "name": "Rachel Green",
         "phone": "075555555", "photo": "", "bio": "Hello", "gender": "2", "sexualPreference": "1"},
        {"username": "TLuke21", "password": "deez", "age": 21, "email": "tluke21@gmail.com", "name": "Tom Luke",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "CTribbiani32", "password": "deez", "age": 32, "email": "ctribbiani22@gmail.com",
         "name": "Chandler Tribbiani",
         "phone": "075555557", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
    ]

    questionnaires = []

    for i in range(len(users)):
        questionnaires.append({"user": users[i], "answers": {"ans1": random.randint(0, 3), "ans2": random.randint(0, 3),
                                                             "ans3": random.randint(0, 3), "ans4": random.randint(0, 3),
                                                             "ans5": random.randint(0, 3),
                                                             "ans6": random.randint(0, 3), "ans7": random.randint(0, 3),
                                                             "ans8": random.randint(0, 3),
                                                             }})

    for user in range(len(users)):
        u = add_user(users[user]["username"], users[user]["password"], users[user]["age"], users[user]["email"], users[user]["name"], users[user]["phone"],
                     users[user]["photo"], users[user]["bio"], users[user]["gender"], users[user]["sexualPreference"])
        add_questionnaire(u, questionnaires[user]["answers"])
        print("Adding ", users[user]["username"], "\n", questionnaires[user]["answers"])


def add_user(username, password, age, email, name, phone, photo, bio, gender, sexualPreference):
    u = UserProfile.objects.get_or_create()[0]
    u.username = username
    u.password = password
    u.age = age
    u.email = email
    u.name = name
    u.phone = phone
    u.photo = photo
    u.bio = bio
    u.gender = gender
    u.sexualPreference = sexualPreference
    u.save()
    return u


def add_questionnaire(user, answers):
    q = Questionnaire.objects.get_or_create()[0]
    q.user = user
    q.answer1 = answers["ans1"]
    q.answer2 = answers["ans2"]
    q.answer3 = answers["ans3"]
    q.answer4 = answers["ans4"]
    q.answer5 = answers["ans5"]
    q.answer6 = answers["ans6"]
    q.answer7 = answers["ans7"]
    q.answer8 = answers["ans8"]
    q.save()
    return q


populate()
