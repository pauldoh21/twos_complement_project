import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twos_complement_project.settings')

import django

django.setup()
from TwosComplement.models import UserProfile, Matches, Questionnaire

random.seed(1564)


def populate():
    users = [

        {"username": "RGreen19", "password": "deez", "age": 19, "email": "rgreen19@gmail.com", "name": "Rachel Green",
         "phone": "075555555", "photo": "", "bio": "Hello", "gender": "2", "sexualPreference": "1"},
        {"username": "TLuke21", "password": "deez", "age": 21, "email": "tluke21@gmail.com", "name": "Tom Luke",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "CTribbiani32", "password": "deez", "age": 32, "email": "ctribbiani22@gmail.com", "name": "Chandler Tribbiani",
         "phone": "075555557", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "BSchmet", "password": "deez", "age": 28, "email": "bschmet@gmail.com", "name": "Brian Schmetzer",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "ymrzn19", "password": "deez", "age": 19, "email": "ymrzn@gmail.com", "name": "Jonathan Morrin",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "tsuth25", "password": "deez", "age": 22, "email": "tsuth@gmail.com", "name": "Tabatha Sutherland",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "DenchJudi", "password": "deez", "age": 27, "email": "jdench@gmail.com", "name": "Judi Dench",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "DuaLipa", "password": "deez", "age": 26, "email": "dulapeep@gmail.com", "name": "Dua Lipa",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "SylvMcc", "password": "deez", "age": 20, "email": "sylv@gmail.com", "name": "Sylvester McCoy",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},
        {"username": "TemMor", "password": "deez", "age": 25, "email": "bobafett@gmail.com", "name": "Temeura Morrison",
         "phone": "075555556", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "2"},

    ]

    questionnaires = []

    for i in range(len(users)):
        questionnaires.append({"user": users[i], "answers": {"ans1": random.randint(1, 4), "ans2": random.randint(1, 4),
                                                             "ans3": random.randint(1, 4), "ans4": random.randint(1, 4),
                                                             "ans5": random.randint(1, 4),
                                                             "ans6": random.randint(1, 12), "ans7": random.randint(1, 3),
                                                             "ans8": random.randint(1, 5), "ans9": random.randint(1, 8),
                                                             "ans10": random.randint(1, 6),
                                                             }})

    for user in range(len(users)):
        u = add_user(users[user]["username"], users[user]["password"], users[user]["age"], users[user]["email"], users[user]["name"], users[user]["phone"],
                     users[user]["photo"], users[user]["bio"], users[user]["gender"], users[user]["sexualPreference"])
        add_questionnaire(u, questionnaires[user]["answers"])
        print("Adding ", users[user]["username"], "\n", questionnaires[user]["answers"], "\n")


def add_user(username, password, age, email, name, phone, photo, bio, gender, sexualPreference):
    u = UserProfile.objects.get_or_create(username=username, age=age, gender=gender, sexualPreference=sexualPreference)[0]
    u.password = password
    u.email = email
    u.name = name
    u.phone = phone
    u.photo = photo
    u.bio = bio
    u.save()
    return u


def add_questionnaire(user, answers):
    q = Questionnaire.objects.get_or_create(Q1=answers["ans1"],
                                            Q2=answers["ans2"],
                                            Q3=answers["ans3"],
                                            Q4=answers["ans4"],
                                            Q5=answers["ans5"],
                                            Q6=answers["ans6"],
                                            Q7=answers["ans7"],
                                            Q8=answers["ans8"],
                                            Q9=answers["ans9"],
                                            Q10=answers["ans10"],
                                            user=user)[0]
    q.save()
    return q


if __name__ == '__main__':
    print('Starting Twos Complement population script...')
    populate()

