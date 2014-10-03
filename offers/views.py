#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, random, sha
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from offers.models import Company

def index(request):
    return render(request, 'offers/index.html')

def createAccount(request):
    return render(request, 'offers/createAccount.html')

def createEmployerAccount(request):
    return render(request, 'offers/createEmployerAccount.html')

def doCreateEmployerAccount(request):
    
    if request.user.is_authenticated():
        # They already have an account; don't let them register again
        return render_to_response('offers/createEmployerAccount.html', {'has_account': True})
    
    if request.POST:
        params = { p:request.POST[p] for p in ['user_lastname', 'user_firstname', 'username', 'password', 'email', 'company_name', 'company_web', 'company_description'] }
        
        # Build the activation key for their account                                                                                                                    
        salt = sha.new(str(random.random())).hexdigest()[:5]
        activation_key = sha.new(salt+params['username']).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)
        
        c = Company.objects.create_company(params, activation_key, key_expires)
        c.user.is_active = False
        c.user.save()
    
        # Send an email with the confirmation link                                                                                                                      
        email_subject = 'Confirmation de la cr�ation de compte chez PartTime'
        email_body = "Bonjour, %s, et merci de vous etre enregistre chez PartTime.fr!\n\nPour activer votre compte, cilquez sur ce lien avant 48 heures:\n\nhttp://127.0.0.1:8000//offers/confirm/%s" % (c.user.username, c.activation_key)
        send_mail(email_subject, email_body, 'no-reply@parttime.fr', [c.user.email])

        return render_to_response('offers/createEmployerAccount.html', {'created': True})
    return render_to_response('offers/index.html')
    
def confirm(request, activation_key):
    if request.user.is_authenticated():
        return render_to_response('confirm.html', {'has_account': True})
    user_profile = get_object_or_404(Company, activation_key=activation_key)
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response('confirm.html', {'expired': True})
    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    return render_to_response('confirm.html', {'success': True})


def createCandidateAccount(request):
    return HttpResponse('non disponible')
    

@login_required
def account(request):
    user_profile = request.user.get_profile()
    url = user_profile.url

    return HttpResponse("Hello, world. You're viewing the page of a user.")

@login_required
def logout_view(request):
    logout(request)
    return index(request)
