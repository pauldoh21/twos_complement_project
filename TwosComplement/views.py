from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from TwosComplement.forms import UserForm, UserProfileForm, QuestionnaireForm


def index(request):
    context_dict = {'boldmessage': 'Hello guys'}
    return render(request, 'TwosComplement/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'This is the about page for our team'}
    return render(request, 'TwosComplement/about_us.html', context=context_dict)


# def login(request):
#    context_dict = {'boldmessage': 'This is the login page'}
#    return render(request, 'TwosComplement/login.html', context=context_dict)


def myDates(request):
    context_dict = {'boldmessage': 'Here is a list of all your matches!'}
    return render(request, 'TwosComplement/my_dates.html', context=context_dict)


# def register(request):
#   context_dict = {'boldmessage': 'Please fill out your details below to register:'}
#  return render(request, 'TwosComplement/register.html', context=context_dict)


def myAccount(request):
    context_dict = {'boldmessage': 'View your profile!'}
    return render(request, 'TwosComplement/my_account.html', context=context_dict)


def manage(request):
    context_dict = {'boldmessage': 'Change any details about your profile here:'}
    return render(request, 'TwosComplement/manage.html', context=context_dict)


def questionnaire(request):
    context_dict = {'boldmessage': 'Please fill out our questionnaire to finish registration:'}
    if request.method == 'POST':
        questionnaire_form = QuestionnaireForm(request.POST)

        if questionnaire_form.is_valid():
            questionnaire = questionnaire_form.save()
            questionnaire.save()
            return redirect('/TwosComplement/index')
        else:
            print(questionnaire_form.errors)
    else:
        questionnaire_form = QuestionnaireForm()
    return render(request, 'TwosComplement/compatibility_questionnaire.html', context={'questionnaire_form': questionnaire_form})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            return redirect('/TwosComplement/register/compatibility_questionnaire/')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'TwosComplement/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('TwosComplement:index'))
            else:
                return HttpResponse("Your Twos Complement account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'TwosComplement/login.html')