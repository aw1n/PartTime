from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'offers/index.html')

def createAccount(request):
    return render(request, 'offers/createAccount.html')

def createEmployerAccount(request):
    return render(request, 'offers/createEmployerAccount.html')

def doCreateEmployerAccount(request):
    return HttpResponse('non disponible')


def createCandidateAccount(request):
    return HttpResponse('non disponible')

@login_required
def account(request):
    return HttpResponse("Hello, world. You're viewing the page of a user.")

@login_required
def logout_view(request):
    logout(request)
    return index(request)
