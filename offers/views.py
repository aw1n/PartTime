from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    template = loader.get_template('offers/index.html')
    return HttpResponse(template.render(RequestContext(request)))

@login_required
def account(request):
    return HttpResponse("Hello, world. You're viewing the page of a user.")
