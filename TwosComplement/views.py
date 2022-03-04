from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': 'Hello guys'}
    return render(request, 'TwosComplement/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'This is the about page for our team'}
    return render(request, 'TwosComplement/about_us.html', context=context_dict)


def login(request):
    context_dict = {'boldmessage': 'This is the login page'}
    return render(request, 'TwosComplement/login.html', context=context_dict)


def myDates(request):
    context_dict = {'boldmessage': 'Here is a list of all your matches!'}
    return render(request, 'TwosComplement/my_dates.html', context=context_dict)


def register(request):
    context_dict = {'boldmessage': 'Please fill out your details below to register:'}
    return render(request, 'TwosComplement/register.html', context=context_dict)


def myAccount(request):
    context_dict = {'boldmessage': 'View your profile!'}
    return render(request, 'TwosComplement/my_account.html', context=context_dict)


def manage(request):
    context_dict = {'boldmessage': 'Change any details about your profile here:'}
    return render(request, 'TwosComplement/manage.html', context=context_dict)


def questionnaire(request):
    context_dict = {'boldmessage': 'Please fill out our questionnaire to finish registration:'}
    return render(request, 'TwosComplement/compatibility_questionnaire.html', context=context_dict)

