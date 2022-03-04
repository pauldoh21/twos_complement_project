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

