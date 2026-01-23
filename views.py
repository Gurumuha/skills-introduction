#add rocky to Django app

from django.shortcuts import render
from django.http import HttpResponse

def rocky (request):
  return HttpResponse ("Welcome to Django!") 
                
