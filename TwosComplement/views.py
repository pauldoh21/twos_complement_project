from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from TwosComplement.models import UserProfile, Matches, Questionnaire
from TwosComplement.forms import UserForm, UserProfileForm, QuestionnaireForm, ManageUserForm, ManageUserProfileForm


# Matching algorithm
def check_match(q1, q2):
    users = UserProfile.objects.all()

    for u in users:
        if q1.user == u.user:
            user1 = u
        if q2.user == u.user:
            user2 = u

    # print(user1.name, user1.sexualPreference, user1.gender, user2.name, user2.sexualPreference, user2.gender)
    # print(user1.sexualPreference == user2.gender)
    if ((user1.sexualPreference == user2.gender) or (user1.sexualPreference == '3')) and ((user2.sexualPreference == user1.gender) or (user2.sexualPreference == '3')):

        q1_ans = {a: b for a, b in vars(q1).items() if a.startswith("Q")}
        q2_ans = {a: b for a, b in vars(q2).items() if a.startswith("Q")}

        # print(q1_ans)
        # print(q2_ans)

        match_score = 0

        for i, j in q1_ans.items():
            # print(q1_ans[i], q2_ans[i])
            if q1_ans[i] == q2_ans[i] and q2.user != q1.user:
                match_score += 1

        if match_score > 3:
            Matches.objects.get_or_create(user1=user1, user2=user2, compatibilityScore=match_score)
            return [user2, match_score]
        else:
            return None

    else:
        return None


def index(request):
    return render(request, 'TwosComplement/index.html')


def about(request):
    context_dict = {'boldmessage': 'This is the about page for our team'}
    return render(request, 'TwosComplement/about_us.html', context=context_dict)


# decorator used for user authentication
# user can only view mydates once they've logged in.
# displays 5 top matches if there are any
@login_required
def myDates(request):

    context_dict = {'boldmessage': 'Here is a list of all your matches!'}

    match_list = Matches.objects.all()
    users = UserProfile.objects.all()
    questionnaires = Questionnaire.objects.all()

    active_user = request.user
    active_user_questionnaire = None

    for q in range(len(questionnaires)):
        # print(questionnaires[q].user, active_user)
        if questionnaires[q].user == active_user:
            active_user_questionnaire = questionnaires[q]

    matches = []

    if active_user_questionnaire is not None:
        for u in range(len(questionnaires)):
            match_check = check_match(active_user_questionnaire, questionnaires[u])
            if match_check is not None:
                matches.append(match_check)

        matches.sort(key=lambda x: x[1], reverse=True)
        context_dict['matches'] = [a[0] for a in matches[:5]]

    return render(request, 'TwosComplement/my_dates.html', context=context_dict)


# decorator used for user authentication
# user can only view myaccount once they've logged in.
@login_required
def myAccount(request):
    current_user = request.user
    current_user_profile = UserProfile.objects.get(user=current_user)
    return render(request, 'TwosComplement/my_account.html', {"user": current_user, "user_profile": current_user_profile})


# decorator used for user authentication
# user can only edit their profile once they're logged in.
@login_required
def manage(request):
    current_user = request.user
    current_user_profile = UserProfile.objects.get(user=current_user)

    user_form = ManageUserForm(request.POST)
    profile_form = ManageUserProfileForm(request.POST, request.FILES)

    if request.method == 'POST':

        print(request.FILES)

        if request.POST['age'] != '':
            current_user_profile.age = request.POST['age']
        if request.POST['name'] != '':
            current_user_profile.name = request.POST['name']
        if request.POST['phone'] != '':
            current_user_profile.phone = request.POST['phone']
        if request.POST['bio'] != '':
            current_user_profile.bio = request.POST['bio']
        if 'photo' in request.FILES:
            if request.FILES['photo'] != '':
                current_user_profile.photo = request.FILES['photo']
        if request.POST['gender'] != '0':
            current_user_profile.gender = request.POST['gender']
        if request.POST['sexualPreference'] != '0':
            current_user_profile.sexualPreference = request.POST['sexualPreference']
        if request.POST['github'] != '':
            current_user_profile.github = request.POST['github']
        if request.POST['discord'] != '':
            current_user_profile.discord = request.POST['discord']

        current_user_profile.save()

        return redirect('TwosComplement:my_dates')

    return render(request, 'TwosComplement/manage.html', context={'user': current_user,
                                                                  'user_profile': current_user_profile,
                                                                  'user_form': user_form,
                                                                  'profile_form': profile_form})


# decorator used for user authentication
# user can only view mydates once they've registered
@login_required
def questionnaire(request):
    context_dict = {'boldmessage': 'Please fill out our questionnaire to finish registration:'}
    if request.method == 'POST':
        questionnaire_form = QuestionnaireForm(request.POST)

        if questionnaire_form.is_valid():
            questionnaire = questionnaire_form.save(commit=False)
            questionnaire.user = request.user
            questionnaire.save()
            return redirect('TwosComplement:index')
        else:
            print(questionnaire_form.errors)
    else:
        questionnaire_form = QuestionnaireForm()
    return render(request, 'TwosComplement/compatibility_questionnaire.html', context={'questionnaire_form': questionnaire_form})


# register view - populates User/UserProfile model and then sends to questionnaire
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

            login(request, user)
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


# login view - uses inbuilt django functions to allow users to login etc
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('TwosComplement:my_dates'))
            else:
                return HttpResponse("Your Twos Complement account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'TwosComplement/login.html')


# decorator used for user authentication
# user can only logout once they've logged in.
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
