from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'FIRSTAPPLICATION/index.html')

def training_domain(request, domain_id):
    return HttpResponse("You are in the id %s" % domain_id)

def candidate(request, domain_id):
    response = "You are the candidate named as %s."
    return HttpResponse(response % domain_id)