import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twos_complement_project.settings')

import django

django.setup()
from django.contrib.auth.models import User
from TwosComplement.models import UserProfile, Matches, Questionnaire

random.seed(1564)


def populate():
    users = [

        {"username": "RGreen19", "password": "ross", "age": 19, "email": "rgreen19@gmail.com", "name": "Rachel Green",
         "phone": "07184763998", "photo": "", "bio": "I just graduated high school and am thinking of doing CS", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "TLuke21", "password": "tom123", "age": 21, "email": "tluke21@gmail.com", "name": "Tom Luke",
         "phone": "07986990201", "photo": "", "bio": "I study CS at university of glasgow", "gender": "1", "sexualPreference": "3", "github": "", "discord": ""},
        {"username": "CTribbiani32", "password": "joey", "age": 32, "email": "ctribbiani22@gmail.com", "name": "Chandler Tribbiani",
         "phone": "07546376512", "photo": "", "bio": "I currently work as a software developer", "gender": "1", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "BSchmet", "password": "brian", "age": 28, "email": "bschmet@gmail.com", "name": "Brian Schmetzer",
         "phone": "07856533425", "photo": "profile_images/brian.jpg", "bio": "I am an application developer at google", "gender": "1", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "ymrzn19", "password": "ymorzin", "age": 19, "email": "ymrzn@gmail.com", "name": "Jonathan Morrin",
         "phone": "07523044912", "photo": "profile_images/ymorzin.jpeg", "bio": "I study software engineering at university of surrey", "gender": "1", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "tsuth25", "password": "987654321", "age": 22, "email": "tsuth@gmail.com", "name": "Tabatha Sutherland",
         "phone": "07812439890", "photo": "", "bio": "I am a self taught programmer i've been interested in programming since highschool", "gender": "2", "sexualPreference": "3", "github": "", "discord": ""},
        {"username": "DenchJudi", "password": "cats", "age": 27, "email": "jdench@gmail.com", "name": "Judi Dench",
         "phone": "07316002367", "photo": "profile_images/judi.webp", "bio": "i am a Phd student at university of birmingham doing HCI", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "DuaLipa", "password": "singing", "age": 26, "email": "dulapeep@gmail.com", "name": "Dua Lipa",
         "phone": "07987831103", "photo": "profile_images/dualipa.png", "bio": "I am a singer however lately i've shifted my interest as i discover all about computers", "gender": "2", "sexualPreference": "2", "github": "dulapeep", "discord": ""},
        {"username": "SylvMcc", "password": "12345", "age": 20, "email": "sylv@gmail.com", "name": "Sylvester McCoy",
         "phone": "07463352871", "photo": "", "bio": "I am just getting into CS and i'd really like to get to know people in the industry", "gender": "1", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "TemMor", "password": "password", "age": 25, "email": "bobafett@gmail.com", "name": "Temeura Morrison",
         "phone": "07513404527", "photo": "profile_images/temuera.jpg", "bio": "I am a site developer at barclays", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "blueblue", "password": "clairefoy", "age": 19, "email": "evablues@gmail.com", "name": "Eva Blues",
         "phone": "07789308249", "photo": "", "bio": "I just joined a beginners course to learn the basics of web app development", "gender": "2", "sexualPreference": "3", "github": "", "discord": ""},
        {"username": "dihaz", "password": "mandykerry", "age": 50, "email": "di_haz@gmail.com", "name": "Diane Hazlett",
         "phone": "07816837988", "photo": "", "bio": "I am a senior developer at facebook", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "HeyElliot", "password": "mrrobot", "age": 26, "email": "mr_robot@gmail.com", "name": "Elliot Alderson",
         "phone": "07123456789", "photo": "", "bio": "I'd really like to meet people in the industry work on projects together", "gender": "1", "sexualPreference": "3", "github": "", "discord": ""},
        {"username": "shoEdgar", "password": "ruaridh", "age": 50, "email": "shonaedgar@gmail.com", "name": "Shona Edgar",
         "phone": "07453098712", "photo": "", "bio": "I am a self employed web app developer", "gender": "2", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "crazyCat", "password": "grease", "age": 20, "email": "andyweirdo@gmail.com", "name": "Andy Roberts",
         "phone": "07853215490", "photo": "", "bio": "I work at a retail store and in my free time i like to work on my own projects", "gender": "1", "sexualPreference": "2", "github": "", "discord": "crazycat"},
        {"username": "propGuy", "password": "prop", "age": 21, "email": "johnnycameron@gmail.com", "name": "Johnny Cameron",
         "phone": "07326415254", "photo": "", "bio": "Hello", "gender": "1", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "Wiz", "password": "england", "age": 19, "email": "wizkid@gmail.com", "name": "Isabel Granger",
         "phone": "07513489527", "photo": "", "bio": "Hello", "gender": "2", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "Chengers", "password": "ellen", "age": 29, "email": "chengerz@gmail.com", "name": "Ian Cheng",
         "phone": "07987654321", "photo": "", "bio": "I am a software developer in a hospital programming machines", "gender": "1", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "Louis", "password": "sophie", "age": 21, "email": "meekster@gmail.com", "name": "Louis Meek",
         "phone": "07485623400", "photo": "", "bio": "I study CS at kings college london", "gender": "1", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "lifeOfCallum", "password": "hannah", "age": 19, "email": "calzo@gmail.com", "name": "Callum Holmes",
         "phone": "09586743251", "photo": "", "bio": "I just graduated school and am thinking of purusuing a CS carrer", "gender": "1", "sexualPreference": "1", "github": "calzo", "discord": ""},
        {"username": "fifi", "password": "ellen", "age": 19, "email": "fifikennedy@gmail.com", "name": "Fiona Kennedy",
         "phone": "07724837462", "photo": "", "bio": "I am a first year CS student at UofG", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "Ellie7", "password": "hollister", "age": 18, "email": "ellmck@gmail.com", "name": "Ellie Mckenna",
         "phone": "07629073836", "photo": "", "bio": "I am at GIC doing foundation for software engineering", "gender": "2", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "holl1ster", "password": "surfboard", "age": 37, "email": "hco@gmail.com", "name": "Holly Ster",
         "phone": "07331320089", "photo": "", "bio": "I work part time developer at bank of scotland and am also a gym manager", "gender": "2", "sexualPreference": "3", "github": "", "discord": ""},
        {"username": "ginganinja", "password": "computing", "age": 45, "email": "mrharris@gmail.com", "name": "Fred Harris",
         "phone": "07987888541", "photo": "profile_images/fred.jpg", "bio": "I am currently unemployed but i have a degree in AI and computer systems", "gender": "1", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "AnnaP", "password": "99loveballoons", "age": 19, "email": "kelpie@gmail.com", "name": "Anna Paterson",
         "phone": "07987218664", "photo": "profile_images/anna.png", "bio": "I graduated from highschool and am taking a gap year to learn python and java languages", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "Theresa1956", "password": "tories", "age": 65, "email": "t_dog@gmail.com", "name": "Theresa May",
         "phone": "07989837284", "photo": "profile_images/theresa.jpg", "bio": "I am currently a retired developer from apple who graduated edinbrugh mechatronics", "gender": "2", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "jimbo98", "password": "tories", "age": 24, "email": "jimmy@gmail.com", "name": "Jim Borne",
         "phone": "07543728323", "photo": "", "bio": "i work at apple as a software developer", "gender": "1", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "divertom", "password": "diving", "age": 28, "email": "tomdaley@gmail.com", "name": "Tom Daley",
         "phone": "07698988418", "photo": "", "bio": "i study software engineering at university of glasgow", "gender": "1", "sexualPreference": "1", "github": "", "discord": ""},
        {"username": "bigNic", "password": "SNP", "age": 40, "email": "frst_mnstr@gmail.com", "name": "Nicola Sturgeon",
         "phone": "07681672639", "photo": "profile_images/nicola_sturgeon.jpg", "bio": "I work a bmw and i help develop the software for the car display system", "gender": "2", "sexualPreference": "2", "github": "", "discord": ""},
        {"username": "bojo", "password": "scumbag", "age": 70, "email": "pm@gov.co.uk", "name": "Boris Johnson",
         "phone": "07666666666", "photo": "", "bio": "I work in artificial intelligence and robot development", "gender": "1", "sexualPreference": "2", "github": "", "discord": ""},
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
        u = add_user(users[user]["username"], users[user]["email"], users[user]["password"], users[user]["age"],
                     users[user]["name"], users[user]["phone"],
                     users[user]["photo"], users[user]["bio"], users[user]["gender"], users[user]["sexualPreference"],
                     users[user]["github"], users[user]["discord"])
        add_questionnaire(u, questionnaires[user]["answers"])
        print("Adding ", users[user]["username"], "\n", questionnaires[user]["answers"], "\n")


def add_user(username, email, password, age, name, phone, photo, bio, gender, sexualPreference, github, discord):
    u = User.objects.create_user(username=username, email=email, password=password)
    u.save()
    up = UserProfile.objects.get_or_create(user=u, age=age, name=name,
                                           phone=phone, photo=photo, bio=bio,
                                           gender=gender, sexualPreference=sexualPreference,
                                           github=github, discord=discord)[0]
    up.save()
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

